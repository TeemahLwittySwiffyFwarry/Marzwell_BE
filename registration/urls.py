from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PupilViewSet

router = DefaultRouter()
router.register(r'pupils', PupilViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
