# Generated by Django 4.2.6 on 2024-08-29 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0006_alter_testimonial_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='approval',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Approval pending', 'Approval pending')], default='pending_approval', max_length=20),
        ),
    ]
