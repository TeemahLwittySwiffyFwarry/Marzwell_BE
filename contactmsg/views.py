from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from .serializers import ContactMessageSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-date_sent')
    serializer_class = ContactMessageSerializer

    @action(detail=False, methods=['post'])
    def send_contact_email(self, request):
        # Extract data from request
        name = request.data.get('name')
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')

        if not all([name, email, subject, message]):
            return Response({'status': 'error', 'message': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Send the email
            send_mail(
                subject=f"Contact Form Submission: {subject}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['recipient@example.com'],  # Replace with the actual recipient email address
                fail_silently=False,
            )
            # Save the contact message
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'Message sent successfully!'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
