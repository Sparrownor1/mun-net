from django import forms
from .models import Country, Committee, Delegate, PositionPaper
from users.models import Delegation

class DelegateForm(forms.ModelForm):
    class Meta:
        model = Delegate

        fields = ['first_name',
                  'last_name',
                  'email',
                  'dob',
                  'past_conferences',
                  'committee_preference',
                  'country_preference',
                  ]

        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'email': 'Email',
                  'dob': 'Date of Birth',
                  'past_conferences': 'No. of Past Conferences',
                  'country_preference': 'Country Preference',
                  'committee_preference': 'Committee Preference',
                  }

        widgets = {"dob": forms.DateInput(attrs={'type': 'date'})}

class DelegationForm(forms.ModelForm):
    class Meta:
        model = Delegation
        fields = ['name',
                  'size',
                  'contact_number']

class PositionPaperForm(forms.ModelForm):
    class Meta:
        model = PositionPaper
        fields = ['document',]
