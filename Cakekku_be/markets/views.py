from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Market, Review
from .serializers import MarketSerializer, ReviewSerializer

class MarketListAPIView(ListAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
