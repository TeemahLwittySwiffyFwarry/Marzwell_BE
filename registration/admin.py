from django.contrib import admin
from .models import Pupil
from import_export.admin import ImportExportModelAdmin

class PupilAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'pupil_name', 'grade', 'age','status')

class PupilAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Pupil, PupilAdmin)
