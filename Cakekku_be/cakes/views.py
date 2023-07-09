from django.shortcuts import render
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cake
from markets.models import Market
from .serializers import CakeSerializer

class CakeCreateAPIView(APIView):
    def post(self,request):
        cake = Cake()
        cake.cake_price = request.data["cake_price"]
        cake.cake_market = Market.objects.get(store_id = request.data.get("cake_market"))
        cake.save()

        market = Market.objects.get(store_id = request.data["cake_market"])
        lower_price = 10_000_000
        higher_price = -1
        for cake in market.cakes.all():
            if cake.cake_price < lower_price:
                lower_price = cake.cake_price
            if cake.cake_price > higher_price:
                higher_price = cake.cake_price
        if lower_price == 10_000_000:
            market.store_lower_price = 0
        else:
            market.store_lower_price = lower_price
        if higher_price == -1:
            market.store_higher_price = 0
        else:
            market.store_higher_price = higher_price
        market.save()
        cake_serializer = CakeSerializer(cake)
        return Response(cake_serializer.data, status=200)