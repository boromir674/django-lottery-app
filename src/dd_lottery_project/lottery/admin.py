from django.contrib import admin
from django.shortcuts import reverse, redirect, render
from django.http import HttpResponseRedirect

from .db_access.models import *
from .db_access.models.participation import PARTICIPATION_STATES
from .forms.competition_form import AddParticipationsForm

from lottery.utils import CodeGenerator

import logging
logger = logging.getLogger(__name__)


class CompetitionAdmin(admin.ModelAdmin):
    model = Competition
    list_display = ('name', 'begin_date', 'end_date', 'is_running', 'all', 'confirmed', 'pct')

    def all(self, obj):
        # return obj.participations.count()
        return len(obj.participations.all())

    def confirmed(self, obj):
        return len(obj.participations.all().filter(state=1))

    def pct(self, obj):
        _ = self.all(obj)
        if _ == 0:
            return '0.0%'
        return '{:.1f}%'.format(100 * self.confirmed(obj) / float(_))

    actions = ['add_random']

    def add_random(self, request, queryset):
        # All requests here will actually be of type POST
        # so we will need to check for our special key 'apply'
        # rather than the actual request type
        form = AddParticipationsForm(request.POST)
        # self.message_user(request, "apply in?: {}".format('apply' in request.POST))
        if 'apply' in request.POST:
            print('-------------------')
            logger.info("'apply' in request.POST")
            # The user clicked submit on the intermediate form.
            # Perform our update action:
            form = AddParticipationsForm(request.POST)
            self.message_user(request, "apply in?: {}".format('apply' in request.POST))
            if form.is_valid():
                self.message_user(request, "VALID form")
                code_generator = CodeGenerator.from_lottery_db(form.cleaned_data['code_length'],
                                                               form.cleaned_data['code_length'], Participation,
                                                           update=True)
                for comp in queryset:
                    print("COMPETITION", comp.id)
                    comp.add_random(code_generator)
                    code_generator.nb_codes = form.nb_codes
                # Redirect to our admin view after our update has
                # completed with a nice little info message saying
                # our models have been updated:
                self.message_user(request, "Add codes to {} competitions".format(queryset.count()))
                return HttpResponseRedirect(request.get_full_path())  # return to CompetitionAdmin page
            else:
                form = AddParticipationsForm()
                self.message_user(request, "Invalid generator settings")

        return render(request,
                      'admin/add_codes_intermediate.html',
                      context={'competitions': queryset,
                               'form': form
                               })

    add_random.short_description = "Add new random codes to the competitions"


        # return redirect(reverse('add_random_participants', args=[queryset]))
        #
        # form = CompetitionForm(request.POST)
        # if form.is_valid():
        #     return HttpResponseRedirect('/competition')
        #
        #     # self.get(request, *args, **kwargs)
        #     # if a GET (or any other method) we'll create a blank form
        # else:
        #     return HttpResponseRedirect('/dd_admin')


        #
        #     form = ParticipationCodeForm()
        # a = HttpResponseRedirect('/competition')
        # for comp in queryset:
        #     comp.add_random()
        #     queryset.objects.new_random(status='p')

    # make_published.short_description = "Mark selected stories as published"
    # actions = ['']
    #
    # def make_published(self, request, queryset):
    #     ParticipationsTable.objects.new_random()
    #     queryset.update(status='p')
    #
    # make_published.short_description = "Mark selected stories as published"


"""
e URL accepts arguments, you may pass them in args. For example:

from django.urls import reverse

def myview(request):
    return HttpResponseRedirect(reverse('arch-summary', args=[1945]))
You can also pass kwargs instead of args. For example:

>>> reverse('admin:app_list', kwargs={'app_label': 'auth'})
'/admin/auth/'
"""

class ParticipationAdmin(admin.ModelAdmin):
    model = Participation


class ParticipationsTableAdmin(admin.ModelAdmin):
    model = ParticipationsTable
    list_display = ('participation', 'competition', 'state')

    # search_fields = ('competition', 'state')

    def state(self, obj):
        return PARTICIPATION_STATES[obj.participation.state][1]

admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Participation, ParticipationAdmin)
admin.site.register(ParticipationsTable, ParticipationsTableAdmin)
