from rest_framework import viewsets, serializers
from django.utils import timezone
from .models import Testimonial
from .serializers import TestimonialSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by('-date_created')
    serializer_class = TestimonialSerializer
    
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        instance = serializer.save()

        # Convert `date_created` to date before comparison
        if instance.date_created and instance.date_created.date() > timezone.now().date():
            raise serializers.ValidationError("The creation date cannot be in the future.")
        
        # Save the instance after any custom logic
        serializer.save()
