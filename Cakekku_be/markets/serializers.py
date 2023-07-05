from .models import Market, Review
from rest_framework import serializers

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market

        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review

        fields = '__all__'