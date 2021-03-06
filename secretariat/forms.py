from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from tinymce.widgets import TinyMCE

from users.models import User
from delegation.models import Committee, Allocation, Country, Committee
from .models import Chair, LogisticsRequest, ProgressSheet


class ChairCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    committee = forms.ModelChoiceField(
        queryset=Committee.objects.all(), required=True)

    class Meta(UserCreationForm.Meta):

        model = User
        fields = ['username', 'email', 'password1', 'password2', 'committee']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_chair = True
        if commit:
            user.save()
            chair = Chair.objects.create(
                user=user, committee=self.cleaned_data['committee'])
        return user


class ProgressSheetForm(forms.ModelForm):

    data = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 30}))

    class Meta:
        model = ProgressSheet
        fields = ['data', ]


class LogisticsRequestForm(forms.ModelForm):

    class Meta:
        model = LogisticsRequest
        fields = ['description', ]


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', ]


class CommitteeForm(forms.ModelForm):
    class Meta:
        model = Committee
        fields = '__all__'


class AllocationForm(forms.ModelForm):
    class Meta:
        model = Allocation
        fields = ['country', ]
