from django import forms


class ParticipationCodeForm(forms.Form):
    participation_code = forms.CharField(label='Your code', max_length=6)

    # def is_valid(self):
    #     running_competitions = Competition.objects.filter(is_running=True)
    #     for comp in running_competitions:
    #         if Participation.objects.get(code=code).state == 3:  # is winner


    def cleaned_data(self):
        self.clean()