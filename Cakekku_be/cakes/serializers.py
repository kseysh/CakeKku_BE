from .models import *
from rest_framework import serializers

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class MyCakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCake
        fields = '__all__'


