from .models import Cake
from rest_framework import serializers

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = '__all__'






