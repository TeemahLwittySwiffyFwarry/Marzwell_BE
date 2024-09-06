from django.contrib import admin
from .models import Testimonial
from import_export.admin import ImportExportModelAdmin

# Define a ModelAdmin class to customize the admin interface
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "relationship_to_school", "testimonial", "approval")
    
class TestimonialAdmin(ImportExportModelAdmin):
    pass

# Register the model and its ModelAdmin class
admin.site.register(Testimonial, TestimonialAdmin)
