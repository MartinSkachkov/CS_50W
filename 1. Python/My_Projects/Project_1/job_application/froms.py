from django import forms
from django.core.exceptions import ValidationError

# Our application form will inherit the functionalities of the Django Form 
class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)
    resume = forms.FileField(required=True)

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if not resume.name.endswith('.pdf'):
                raise ValidationError('The file must be a PDF.')
        return resume