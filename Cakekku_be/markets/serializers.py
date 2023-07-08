from .models import Market, Review
from rest_framework import serializers

class MarketSerializer(serializers.ModelSerializer):
    store_like_count = serializers.SerializerMethodField()
    store_average_score = serializers.SerializerMethodField()
    store_lower_price = serializers.SerializerMethodField()
    store_higher_price = serializers.SerializerMethodField()

    def get_store_like_count(self,obj):
        return obj.store_like_people.count()
    
    def get_store_average_score(self, obj):
        count = 0
        total_sum = 0
        average = 0
        for review in obj.reviews.all():
            count += 1
            total_sum += review.review_score
        if count!=0:
            average = total_sum / count
        return average
    
    def get_store_lower_price(self, obj):
        lower_score = 10_000_000
        for cake in obj.cakes.all():
            if cake.cake_price < lower_score:
                lower_score = cake.cake_price
        if lower_score == 10_000_000:
            return 0
        else:
            return lower_score
        
    def get_store_higher_price(self, obj):
        higher_score = -1
        for cake in obj.cakes.all():
            if cake.cake_price > higher_score:
                higher_score = cake.cake_price
        if higher_score == -1:
            return 0
        else:
            return higher_score
        
    class Meta:
        model = Market
        exclude = ['store_like_people']
        extra_fields = ['store_like_count','store_average_score','store_lower_price','store_higher_price']

class OrderingLowerPriceMarketSerializer(MarketSerializer):

    class Meta(MarketSerializer.Meta):
        ordering = ['store_lower_price']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
