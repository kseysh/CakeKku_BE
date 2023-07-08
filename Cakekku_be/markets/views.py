from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Market, Review
from .serializers import MarketSerializer, ReviewSerializer, OrderingLowerPriceMarketSerializer

class MarketListAPIView(ListAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class MarketRetrieveAPIView(RetrieveAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class OrderingLowerPriceMarketRetrieveAPIView(ListAPIView):
    queryset = Market.objects.all()
    serializer_class = OrderingLowerPriceMarketSerializer