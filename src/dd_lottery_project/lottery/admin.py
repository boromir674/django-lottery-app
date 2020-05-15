from django.contrib import admin
# Register your models here.

from .db_access.models import *
from .db_access.models.participation import PARTICIPATION_STATES

from django.http import HttpResponseRedirect
from .forms.competition_form import CompetitionForm


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

    actions = ['new_random']

    def new_random(self, request, queryset):
        form = CompetitionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/competition')

            # self.get(request, *args, **kwargs)
            # if a GET (or any other method) we'll create a blank form
        else:
            return HttpResponseRedirect('/dd_admin')
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
