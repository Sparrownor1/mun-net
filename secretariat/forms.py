from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from delegation.models import Committee
from .models import Chair, LogisticsRequest

class ChairCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    committee = forms.ModelChoiceField(queryset=Committee.objects.all(), required=True)

    class Meta(UserCreationForm.Meta):

        model = User
        fields = ['username', 'email', 'password1', 'password2', 'committee']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_chair = True
        if commit:
            user.save()
            chair = Chair.objects.create(user=user, committee=self.cleaned_data['committee'])
        return user

class LogisticsRequestForm(forms.ModelForm):

    class Meta:
        model = LogisticsRequest
        fields = ['description',]
