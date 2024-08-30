# Generated by Django 4.2.6 on 2024-08-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_alter_pupil_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Contacted', 'Contacted'), ('Awaiting Exam', 'Awaiting Exam'), ('Admitted', 'Admitted')], default='Processing', max_length=20),
        ),
    ]
