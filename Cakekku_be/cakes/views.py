from django.shortcuts import render
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cake
from markets.models import Market
from .serializers import CakeSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi 

class CakeCreateAPIView(APIView):
    cake_price = openapi.Parameter('cake_price', openapi.IN_QUERY, description='cake_price', required=True, type=openapi.TYPE_INTEGER)
    cake_market = openapi.Parameter('cake_market', openapi.IN_QUERY, description='cake_market', required=True, type=openapi.TYPE_INTEGER)
    cake_shape = openapi.Parameter('cake_shape', openapi.IN_QUERY, description='cake_shape', required=True, type=openapi.TYPE_INTEGER)
    cake_image = openapi.Parameter('cake_image', openapi.IN_QUERY, description='cake_image', required=True, type=openapi.TYPE_FILE)

    @swagger_auto_schema(tags=['케이크 만드는 기능'],manual_parameters=[cake_price, cake_market,cake_shape, cake_image], responses={200: 'Success'})
    def post(self,request):
        cake = Cake()
        cake.cake_price = request.data["cake_price"]
        cake.cake_market = Market.objects.get(store_id = request.data.get("cake_market"))
        cake.cake_shape = request.data["cake_shape"]
        cake.cake_image = request.data["cake_image"]

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