from rest_framework import serializers
from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'relationship_to_school', 'testimonial', 'rating', 'image', 'date_created', 'date_modified']
