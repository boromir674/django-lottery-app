from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import *
from .models.participation import PARTICIPATION_STATES
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
        if 'apply' in request.POST:
            logger.info("'apply' in request.POST")
            # The user clicked submit on the intermediate form.
            # Perform our update action:
            form = AddParticipationsForm(request.POST)
            self.message_user(request, "apply in?: {}".format('apply' in request.POST))
            if form.is_valid():
                self.message_user(request, "VALID form")
                code_generator = CodeGenerator.from_lottery_db(form.cleaned_data['code_length'],
                                                               form.cleaned_data['nb_codes'], Participation,
                                                           update=True)
                assert set(code_generator.seen_codes) == set([p.code for p in Participation.objects.all()])
                for comp in queryset:
                    ParticipationsTable.objects.new_random(comp, code_generator)
                    code_generator.nb_codes = form.cleaned_data['nb_codes']
                # Redirect to our admin view after our update has
                # completed with a nice little info message saying
                # our models have been updated:
                self.message_user(request, "Added {} random codes for each of the {} competitions".format(form.cleaned_data['nb_codes'], queryset.count()))
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
