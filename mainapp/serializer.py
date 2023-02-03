from rest_framework import serializers
from mainapp.models import Courses

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Courses
        fields=(
            'id','name','description','start_date',
        )
        