# Generated by Django 5.1 on 2024-08-17 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='relationship_to_school',
            field=models.CharField(choices=[('Parent', 'Parent'), ('Pupils', 'Pupils'), ('Teacher', 'Teacher'), ('Alumni', 'Alumni'), ('Others', 'Others')], help_text='e.g., Parent, Student, Teacher', max_length=20),
        ),
    ]
