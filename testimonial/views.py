from rest_framework import viewsets
from .models import Testimonial
from .serializers import TestimonialSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    def perform_create(self, serializer):
        # Automatically set the `date_created` field only when creating a new instance
        serializer.save(date_created=self.request.data.get('date_created', None))

    def perform_update(self, serializer):
        # Allow updates to the `date_created` field
        serializer.save()
