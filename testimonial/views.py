from rest_framework import viewsets
from .models import Testimonial
from .serializers import TestimonialSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by('-date_created')
    serializer_class = TestimonialSerializer
    
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        # Perform custom validation or logic if needed
        instance = serializer.save()

        # Example: Prevent setting `date_created` to a future date
        if instance.date_created and instance.date_created > timezone.now().date():
            raise serializers.ValidationError("The creation date cannot be in the future.")

        # Save the instance after any custom logic
        serializer.save()
