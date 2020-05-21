from django.views import View
from django.shortcuts import render

from ..forms.code_form import ParticipationCodeForm

import logging

logger = logging.getLogger(__name__)


class CodeChecker(View):

    def post(self, request, *args, **kwargs):
        form = ParticipationCodeForm(request.POST)
        if form.is_valid():
            return self.get(request, *args, **kwargs)
            # if a GET (or any other method) we'll create a blank form
        else:
            form = ParticipationCodeForm()
        return render(request, 'index.html', {'form': form})

    def get(self, request, *args, **kwargs):
        # Render the HTML template index.html with the data in the context variable (eg a templating engine can use them)
        return render(request, 'index.html', context={})


# def build_response(request, html, template_loader, context={'next': '/'}):
#     template = template_loader.get_template(html)
#     return HttpResponse(template.render(context, request))

