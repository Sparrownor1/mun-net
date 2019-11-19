from django.contrib import admin
from .models import Conference, Domain
from django_tenants.admin import TenantAdminMixin
# Register your models here.
class ConferenceAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name',)

admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Domain)
