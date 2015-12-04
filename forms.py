from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.forms.extras.widgets import SelectDateWidget

from .models import Requirement, Testing_Procedure, Merchant


   

class NameForm(forms.Form):
    req_status_choices = (
        ('Not In Place', 'Not In Place'),
        ('In Place', 'In Place'),
        ('In Progress', 'In Progress'),
        ('Not Applicable', 'Not Applicable')
    )
    
    finding_text = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField(choices = req_status_choices )
    


