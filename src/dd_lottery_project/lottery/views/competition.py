from django.views import View

from ..db_access.models.competition import Competition


class CompetitionResource(View):

    def get(self):
        pass

    def post(self, request, *args, **kwargs):
        Competition.objects.new_random()

