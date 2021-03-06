from django import forms
from django.contrib.auth.models import User

from JQ.models import Application, Company, Resources, Notes, Contact, Questions, Ask


class DateInput(forms.DateInput):
    input_type = 'date'

class CreateCompany(forms.ModelForm):

    class Meta:
        model = Company
        exclude = {'user','isDeleted'}

class CreateApplication(forms.ModelForm):

    class Meta:
        model = Application
        exclude = {'user','isDeleted'}
        widgets = {
            'applied_date': forms.DateInput(attrs={'id': 'datetimepicker1', 'class':'form-control','type':'date'})
        }
    def __init__(self, user, *args, **kwargs):
       super(CreateApplication, self).__init__(*args, **kwargs)
       self.fields['company'] = forms.ModelChoiceField(
       queryset=Company.objects.filter(user=user))

class CreateResource(forms.ModelForm):

    class Meta:
        model = Resources
        exclude = {'isDeleted',
                    'App'}

class CreateNote(forms.ModelForm):

    class Meta:
        model = Notes
        exclude = {'isDeleted','App'}

class CreateContact(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = {'isDeleted','App'}

class CreateQuestion(forms.ModelForm):

    class Meta:
        model = Questions
        exclude = {'isDeleted','user'}
