from django.views import View
from django.shortcuts import render, redirect, reverse

from lottery.forms.competition_form import AddParticipationsForm
from lottery.utils import CodeGenerator
from participation import Participation


class CompetitionResource(View):

    def get(self, request, *args, **kwargs):
        if not args or not args[0]:
            redirect(reverse('lottery_admin'))
        print(args[0])
        # context = {'queryset': args[0], 'next': request.GET.get('next', '/')}
        context = {'queryset': [comp.id for comp in args[0]], 'next': request.GET.get('next', '/')}

        return render(request, 'add_participants.html', context=context)


    def post(self, request, *args, **kwargs):
        form = AddParticipationsForm(request.POST)
        if form.is_valid():
            code_generator = CodeGenerator.from_lottery_db(form.code_length, form.nb_codes, Participation, update=True)
            for comp in request.META['queryset']:
                comp.add_random(code_generator=code_generator)
                code_generator.nb_codes = form.nb_codes
