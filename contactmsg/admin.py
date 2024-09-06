from django.contrib import admin
from .models import ContactMessage
from import_export.admin import ImportExportModelAdmin


# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    
class ContactMessageAdmin(ImportExportModelAdmin):
    pass

admin.site.register(ContactMessage, ContactMessageAdmin)