from rest_framework import serializers
from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'relationship_to_school', 'testimonial', 'image', 'date_created', 'rating', 'approval']
        # Removed read_only_fields to make date_created editable
