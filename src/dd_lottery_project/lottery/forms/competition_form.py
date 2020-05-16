from django import forms


class AddParticipationsForm(forms.Form):
    nb_codes = forms.IntegerField(min_value=1, initial=20, max_value=5000, required=True, label='The number of codes to generate')
    code_length = forms.IntegerField(min_value=3, initial=6, max_value=20, required=True, label="The number of the code's characters")
