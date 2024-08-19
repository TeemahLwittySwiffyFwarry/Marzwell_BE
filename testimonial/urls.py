from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestimonialViewSet

router = DefaultRouter()
router.register(r'testimonial', TestimonialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
