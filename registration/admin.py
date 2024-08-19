from django.contrib import admin
from .models import Pupil

class PupilAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'pupil_name', 'grade', 'age','status')

admin.site.register(Pupil, PupilAdmin)
