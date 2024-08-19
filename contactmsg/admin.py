from django.contrib import admin
from .models import ContactMessage

# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

admin.site.register(ContactMessage, ContactMessageAdmin)