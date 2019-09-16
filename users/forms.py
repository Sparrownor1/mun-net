from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Delegation
from django.contrib.auth import get_user_model

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'is_delegation', 'is_chair',
                  'is_secretariat', 'password1', 'password2')

class NewUserChangeForm(UserChangeForm):

    class Meta:

        model = User

        fields = ['email',
                  'first_name',
                  'last_name',
                  'password']

class DelegationSignUpForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):

        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_delegation = True
        if commit:
            user.save()
            delegation = Delegation.objects.create(user=user)
        return user
