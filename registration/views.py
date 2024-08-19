from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, BasePermission
from .models import Pupil
from .serializers import PupilSerializer

class IsAdminUserOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to delete.
    """

    def has_permission(self, request, view):
        # Allow read operations for everyone
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Allow write operations for authenticated users
        if request.method in ['POST', 'PUT', 'PATCH']:
            return True
        
        # Allow delete only for admin users
        if request.method == 'DELETE':
            return request.user and request.user.is_staff
        
        return False

class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request, *args, **kwargs):
        """
        Allow anyone to add a new pupil.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Allow only admin users to delete a pupil.
        """
        if request.user.is_staff:
            return super().destroy(request, *args, **kwargs)
        return Response({'detail': 'Not authorized to delete.'}, status=status.HTTP_403_FORBIDDEN)
