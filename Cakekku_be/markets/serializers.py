from .models import *
from rest_framework import serializers

class MarketSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Market
        exclude = ['store_like_people']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class CakeSizeSerailizer(serializers.ModelSerializer):
    class Meta:
        model = CakeSize
        fields = '__all__'

class BreadSandingSerailizer(serializers.ModelSerializer):
    class Meta:
        model = BreadSanding
        fields = '__all__'
