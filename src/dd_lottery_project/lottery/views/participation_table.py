from django.views import View

from ..db_access.models.participations_table import ParticipationsTable


class CompetitionResource(View):

    def get(self):
        pass

    def post(self, request, *args, **kwargs):
        