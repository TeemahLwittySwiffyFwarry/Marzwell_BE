from rest_framework import serializers
from .models import Pupil

class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = ['id', 'parent_name', 'pupil_name', 'grade', 'age', 'phone_number', 'date_registered', 'status']
