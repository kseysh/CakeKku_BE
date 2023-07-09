from .models import Market, Review
from rest_framework import serializers

class MarketSerializer(serializers.ModelSerializer):    
    # def get_store_lower_price(self, obj):
    #     lower_score = 10_000_000
    #     for cake in obj.cakes.all():
    #         if cake.cake_price < lower_score:
    #             lower_score = cake.cake_price
    #     if lower_score == 10_000_000:
    #         return 0
    #     else:
    #         return lower_score
        
    # def get_store_higher_price(self, obj):
    #     higher_score = -1
    #     for cake in obj.cakes.all():
    #         if cake.cake_price > higher_score:
    #             higher_score = cake.cake_price
    #     if higher_score == -1:
    #         return 0
    #     else:
    #         return higher_score
        
    class Meta:
        model = Market
        exclude = ['store_like_people']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

        
