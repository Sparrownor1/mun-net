from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User, Delegation
from .forms import DelegationSignUpForm, NewUserChangeForm, UserCreationForm

class UserAdmin(UserAdmin):

    add_form = UserCreationForm
    form = NewUserChangeForm

    list_display = ['username', 'email', 'is_secretariat', 'is_chair', 'is_delegation',]
    list_filter = ['is_superuser', 'is_staff', 'is_secretariat', 'is_chair', 'is_delegation',]

    fieldsets = (
        (None, {'fields': ('username', 'password', 'is_delegation', 'is_chair', 'is_secretariat')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        # (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_chair', 'is_secretariat'),
        }),
    )

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Delegation)
