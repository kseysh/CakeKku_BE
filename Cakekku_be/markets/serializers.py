from .models import Market, Review
from rest_framework import serializers

class MarketSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Market
        exclude = ['store_like_people']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

        
