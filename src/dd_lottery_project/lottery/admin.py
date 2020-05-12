from django.contrib import admin
# Register your models here.

from .db_access.models import *
from .db_access.models.participation import PARTICIPATION_STATES


class CompetitionAdmin(admin.ModelAdmin):
    model = Competition
    list_display = ('name', 'begin_date', 'end_date', 'is_running')

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
