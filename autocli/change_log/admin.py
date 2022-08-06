# Django Import:
from django.contrib import admin

# Model Import:
from change_log.models import ChangeLog

# Register your models here.
@admin.register(ChangeLog)
class ChangeLogAdmin(admin.ModelAdmin):

    list_display = (
        'action', 'item_id', 'object_name',
    )
    list_filter = (
        'action',
    )
    search_fields = (
        'item_id', 'object_name', 'after',
    )
    fieldsets = (
        ('Basic settings', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('action', 'item_id', 'object_name')
        }),
        ('Changes', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('after',)
        }),
    )
