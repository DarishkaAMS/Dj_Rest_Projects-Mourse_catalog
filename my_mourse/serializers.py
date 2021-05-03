from rest_framework import serializers

from .models import Mourse


class MourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mourse
        fields = '__all__'
