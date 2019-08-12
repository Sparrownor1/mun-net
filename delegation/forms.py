from django import forms
from .models import Country, Committee, Delegate
from users.models import Delegation

class DelegateForm(forms.ModelForm):

    class Meta:

        model = Delegate

        fields = ['delegate_first_name',
                  'delegate_last_name',
                  'delegate_email',
                  'delegate_dob',
                  'delegate_past_conferences',
                  'delegate_committee_preference',
                  'delegate_country_preference',
                  ]

        labels = {'delegate_first_name': 'First Name',
                  'delegate_last_name': 'Last Name',
                  'delegate_email': 'Email',
                  'delegate_dob': 'Date of Birth',
                  'delegate_past_conferences': 'No. of Past Conferences',
                  'delegate_country_preference': 'Country Preference',
                  'delegate_committee_preference': 'Committee Preference',
                  }

        widgets = {"delegate_dob": forms.DateInput(attrs={'type': 'date'})}

class DelegationForm(forms.ModelForm):

    class Meta:

        model = Delegation

        fields = ['delegation_name',
                  'delegation_size',
                  'delegation_contact_number']
