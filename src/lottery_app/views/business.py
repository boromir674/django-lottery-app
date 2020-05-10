from django.views import View


from django import forms

class BusinessInfoForm(forms.Form):
    name = forms.CharField(label='business name')  # should use the TextInput widget
    description = forms.CharField(label='business description')
    email = forms.EmailField(label='email address')  # should use EmailInput as Widget
    address = forms.CharField(label='physical address')
    receit_specs = forms.FloatField(label='receit width in cm', min_value=1.2)


class InputBusinessInfo(View):

    def post(self):
        pass

    def put(self):
        pass

    def get(self):
        pass
