from django.views import View
from django import forms


class ParticipationCodeForm(forms.Form):
    participation_code = forms.CharField(label='Your code', max_length=6)


class CodeChecker(View):

    def post(self, request):
        form = ParticipationCodeForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

            # if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()

        return render(request, 'name.html', {'form': form})

    def get(self, request, *args, **kwargs):
        return self.post( )

