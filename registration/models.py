from django.db import models

class Pupil(models.Model):
    # Define age choices as a tuple of tuples
    AGE_CHOICES = [(str(i), str(i)) for i in range(2, 13)]

    # Define grade choices
    GRADE_CHOICES = [
        ('toddler_1', 'Toddler 1'),
        ('toddler_2', 'Toddler 2'),
        ('junior_infant', 'Junior Infant'),
        ('senior_infant', 'Senior Infant'),
        ('year_one', 'Year One'),
        ('year_two', 'Year Two'),
        ('year_three', 'Year Three'),
        ('year_four', 'Year Four'),
        ('year_five', 'Year Five'),
    ]
    
    STATUS_CHOICES = [
    ('processing', 'Processing'),
    ('contacted', 'Contacted'),
    ('awaiting_exam', 'Awaiting Exam'),
    ('admitted', 'Admitted'),
]


    parent_name = models.CharField(max_length=100)
    pupil_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES)
    age = models.CharField(max_length=2, choices=AGE_CHOICES)
    phone_number = models.CharField(max_length=15)
    date_registered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')

    def __str__(self):
        return f"Mr/Mrs. {self.parent_name} is registering {self.pupil_name} in {self.grade}"
