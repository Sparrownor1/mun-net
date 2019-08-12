from django.contrib import admin
from .models import Chair, ProgressSheet, LogisticsRequest
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class SheetAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Content", {'fields': ('data',)}),
    )

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
        }

class RequestAdmin(admin.ModelAdmin):

    list_display = ['committee', 'timestamp', 'description', 'completed']
    list_filter = ['committee', 'completed']

    date_hierarchy = 'timestamp'

admin.site.register(Chair)
admin.site.register(ProgressSheet, SheetAdmin)
admin.site.register(LogisticsRequest, RequestAdmin)
