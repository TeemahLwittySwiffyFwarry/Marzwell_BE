from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Pupil
from .serializers import PupilSerializer

class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer

    def get_permissions(self):
        if self.request.method in ['POST']:
            # Allow any user to create a pupil
            permission_classes = [AllowAny]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            # Require authentication for update and delete
            permission_classes = [IsAuthenticated]
        else:
            # For other methods (GET, HEAD, OPTIONS), allow access
            permission_classes = [AllowAny]
        
        return [permission() for permission in permission_classes]

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
        Allow only authenticated users to delete a pupil.
        """
        if request.user.is_authenticated:
            return super().destroy(request, *args, **kwargs)
        return Response({'detail': 'Not authorized to delete.'}, status=status.HTTP_403_FORBIDDEN)
