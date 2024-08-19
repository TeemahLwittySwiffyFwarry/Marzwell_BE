from rest_framework import viewsets
from .models import Testimonial
from .serializers import TestimonialSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by('-date_created')
    serializer_class = TestimonialSerializer
    

    def perform_create(self, serializer):
        serializer.save()
