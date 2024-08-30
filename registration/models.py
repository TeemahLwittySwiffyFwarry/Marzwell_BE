from django.db import models

class Pupil(models.Model):
    # Define age choices as a tuple of tuples
    AGE_CHOICES = [(str(i), str(i)) for i in range(2, 13)]

    # Define grade choices
    GRADE_CHOICES = [
        ('Toddler One', 'Pre-Nursery'),
        ('Toddler Two', 'Nursery One'),
        ('Junior Infant', 'Nursery Two'),
        ('Senior Infant', 'Kindergarten'),
        ('Year One', 'Primary Two'),
        ('Year Two', 'Primary Three'),
        ('Year Three', 'Primary Four'),
        ('Year Four', 'Primary Five'),
        ('Year Five', 'Primary Six'),
    ]
    
    STATUS_CHOICES = [
    ('Processing', 'Processing'),
    ('Contacted', 'Contacted'),
    ('Awaiting Exam', 'Awaiting Exam'),
    ('Admitted', 'Admitted'),
]


    parent_name = models.CharField(max_length=100)
    pupil_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES)
    age = models.CharField(max_length=2, choices=AGE_CHOICES)
    phone_number = models.CharField(max_length=15)
    date_registered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Processing')

    def __str__(self):
        return f"Mr/Mrs. {self.parent_name} is registering {self.pupil_name} in {self.grade}"
