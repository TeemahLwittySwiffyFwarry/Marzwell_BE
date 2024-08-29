from django.db import models

class Testimonial(models.Model):
    # Define the choices for the relationship field
    PARENT = 'Parent'
    PUPIL = 'Pupils'
    TEACHER = 'Teacher'
    ALUMNI = 'Alumni'
    OTHERS = 'Others'
    GUARDIAN = 'Guardian'
    
    RELATIONSHIP_CHOICES = [
        (PARENT, 'Parent'),
        (PUPIL, 'Pupils'),
        (TEACHER, 'Teacher'),
        (ALUMNI, 'Alumni'),
        (OTHERS, 'Others'),
        (GUARDIAN, 'Guardian'),
    ]
    
    approved = 'Approved'
    pending_approval = 'Approval pending'
    
    APPROVAL_CHOICES = [
        (approved, 'Approved'),
        (pending_approval, 'Approval pending'),
    ]
    
    name = models.CharField(max_length=100)
    relationship_to_school = models.CharField(
        max_length=20,
        choices=RELATIONSHIP_CHOICES,
        help_text="e.g., Parent, Student, Teacher"
    )
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=5)
    approval = models.CharField(max_length=20, choices=APPROVAL_CHOICES, default='pending_approval')

    def __str__(self):
        return f"{self.relationship_to_school} {self.name}"
