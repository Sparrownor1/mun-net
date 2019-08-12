from django.contrib import admin
from .models import *

class DelegateAdmin(admin.ModelAdmin):
    list_filter = ['delegate_delegation', ]

class AllocationAdmin(admin.ModelAdmin):
    list_filter = ['allocated_committee', 'allocated_country']

# Register your models here.
admin.site.register(Country)
admin.site.register(Committee)
admin.site.register(Delegate, DelegateAdmin)
admin.site.register(CountryCommitteeAllocation, AllocationAdmin)
