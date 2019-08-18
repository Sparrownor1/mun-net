from django.contrib import admin
from .models import *

class DelegateAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'delegation', 'email', 'dob', 'past_conferences',]
    list_filter = ['delegation', ]

class AllocationAdmin(admin.ModelAdmin):
    list_filter = ['committee', 'country']

class PaperAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'delegate', 'uploaded_at']
    list_filter = ['delegate__allocation__committee',]

# Register your models here.
admin.site.register(Country)
admin.site.register(Committee)
admin.site.register(Delegate, DelegateAdmin)
admin.site.register(Allocation, AllocationAdmin)
admin.site.register(PositionPaper, PaperAdmin)
