from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import Cake, OrderDetail
from markets.models import Market
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi 

class CakeCreateAPIView(APIView):
    @swagger_auto_schema(tags=['고정 디자인 케이크 만드는 기능'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'cake_price': openapi.Schema(type=openapi.TYPE_INTEGER, description='cake_price'),
            'cake_market': openapi.Schema(type=openapi.TYPE_INTEGER, description='cake_market'),
            'cake_shape': openapi.Schema(type=openapi.TYPE_INTEGER, description='cake_shape'),
            'cake_image': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY, description='cake_image'),
        },
        required=['cake_price', 'cake_market', 'cake_shape', 'cake_image']
    ), responses={200: 'Success'})
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
    
class OrderDetailCreateAPIView(CreateAPIView):
    serializer_class = OrderDetailSerializer