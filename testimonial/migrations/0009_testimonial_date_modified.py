# Generated by Django 4.2.6 on 2024-08-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0008_alter_testimonial_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
