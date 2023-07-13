from django.shortcuts import render
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Market, Review
from .serializers import MarketSerializer, ReviewSerializer
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from .models import Market
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi  
from cakes.models import OrderDetail
from cakes.serializers import OrderDetailSerializer, MyCakeSerializer

class MarketListAPIView(APIView):
    order = openapi.Parameter('order', openapi.IN_QUERY, description='review_count / lower_price / higher_price / score / 입력값이 없을 시 일반 ', required=True, type=openapi.TYPE_STRING)
    @swagger_auto_schema(tags=['마켓의 전체 리스트를 불러오는 기능'],manual_parameters=[order], responses={200: 'Success'})
    def get(self, request):
        order_condition = request.GET.get('order',None)
        if order_condition == 'review_count':
            markets = Market.objects.annotate(review_count=Count('reviews')).order_by('-review_count')
        elif order_condition == 'lower_price':
            markets = Market.objects.order_by('store_lower_price')
        elif order_condition == 'higher_price':
            markets = Market.objects.order_by('-store_lower_price')


        elif order_condition == 'score':
            markets = Market.objects.order_by('-store_average_score')
        else:
            markets = Market.objects.all()
        marketSerializer = MarketSerializer(markets, many=True)
        return Response(marketSerializer.data, status=200)
    
@swagger_auto_schema(tags=['특정 마켓 정보 불러오는 기능'], responses={200: 'Success'})
class MarketRetrieveAPIView(RetrieveAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class MarketLike(APIView):
    #store_id = openapi.Parameter('store_id', openapi.IN_QUERY, description='store_id', required=True, type=openapi.TYPE_STRING)
    #@swagger_auto_schema(tags=['마켓에 좋아요 누르는 기능'],manual_parameters=[store_id], responses={200: 'Success'})
    def post(self, request):
        market = Market.objects.get(store_id = request.data["store_id"])
        if request.user in market.store_like_people.all():
            market.store_like_people.remove(request.user)
        else:
            market.store_like_people.add(request.user)
        return Response({"message":market.store_like_people.count()})
    

class ReviewCreateAPIView(APIView):
    review_content = openapi.Parameter('review_content', openapi.IN_QUERY, description='review_content', required=True, type=openapi.TYPE_STRING)
    review_market = openapi.Parameter('review_market', openapi.IN_QUERY, description='review_market', required=True, type=openapi.TYPE_INTEGER)
    review_tag1= openapi.Parameter('review_tag1', openapi.IN_QUERY, description='review_tag1', required=True, type=openapi.TYPE_BOOLEAN)
    review_tag2= openapi.Parameter('review_tag2', openapi.IN_QUERY, description='review_tag2', required=True, type=openapi.TYPE_BOOLEAN)
    review_tag3= openapi.Parameter('review_tag3', openapi.IN_QUERY, description='review_tag3', required=True, type=openapi.TYPE_BOOLEAN)
    review_tag4= openapi.Parameter('review_tag4', openapi.IN_QUERY, description='review_tag4', required=True, type=openapi.TYPE_BOOLEAN)
    review_tag5= openapi.Parameter('review_tag5', openapi.IN_QUERY, description='review_tag5', required=True, type=openapi.TYPE_BOOLEAN)
    review_score = openapi.Parameter('review_score', openapi.IN_QUERY, description='review_score', required=True, type=openapi.TYPE_INTEGER)
    

    @swagger_auto_schema(tags=['리뷰 생성'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'review_image1': openapi.Schema(type=openapi.TYPE_FILE, description='review_image1'),
            'review_image2': openapi.Schema(type=openapi.TYPE_FILE, description='review_image2'),
            'review_image3': openapi.Schema(type=openapi.TYPE_FILE, description='review_image3'),
            'review_image4': openapi.Schema(type=openapi.TYPE_FILE, description='review_image4'),
            'review_image5': openapi.Schema(type=openapi.TYPE_FILE, description='review_image5'),
            'review_content': openapi.Schema(type=openapi.TYPE_STRING, description='review_content'),
            'review_market': openapi.Schema(type=openapi.TYPE_INTEGER, description='review_market'),
            'review_tag1': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='review_tag1'),
            'review_tag2': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='review_tag2'),
            'review_tag3': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='review_tag3'),
            'review_tag4': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='review_tag4'),
            'review_tag5': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='review_tag5'),
            'review_score': openapi.Schema(type=openapi.TYPE_INTEGER, description='review_score'),
        },
        required=['review_image1','review_image2','review_image3','review_image4','review_image5','review_content', 'review_market', 'review_tag1', 'review_tag2', 'review_tag3', 'review_tag4', 'review_tag5', 'review_score']
    ), responses={200: 'Success'})
    def post(self, request):
        review = Review()
        review.review_image1 = request.data.get("review_image1")
        review.review_image2 = request.data.get("review_image2")
        review.review_image3 = request.data.get("review_image3")
        review.review_image4 = request.data.get("review_image4")
        review.review_image5 = request.data.get("review_image5")
        review.review_content = request.data.get("review_content")
        review.review_market = Market.objects.get(store_id=request.data.get("review_market"))
        review.review_tag1 = request.data.get("review_tag1")
        review.review_tag2 = request.data.get("review_tag2")
        review.review_tag3 = request.data.get("review_tag3")
        review.review_tag4 = request.data.get("review_tag4")
        review.review_tag5 = request.data.get("review_tag5")
        review.review_score = request.data.get("review_score")
        review.save()

        reviewed_market = Market.objects.get(store_id=request.data["review_market"])
        total_sum = 0
        count = 0
        average = 0
        for reviewByMarket in reviewed_market.reviews.all():
            total_sum += reviewByMarket.review_score
            count += 1
        if count != 0:
            average = total_sum / count
        reviewed_market.store_average_score = average
        reviewed_market.save()

        review_serializer = ReviewSerializer(reviewByMarket)
        return Response(review_serializer.data, status=200)

class MyReviewList(APIView):
    @swagger_auto_schema(tags=['내 리뷰 조회기능'], responses={200: 'Success'})
    def get(self, request):
        reviews = Review.objects.filter(review_writer = request.user)
        review_serializer = ReviewSerializer(reviews, many=True)
        return Response(review_serializer.data, status=200)
        

search = openapi.Parameter('search', openapi.IN_QUERY, description='search', required=True, type=openapi.TYPE_STRING)
@swagger_auto_schema(tags=['마켓 검색 기능 - get만 쓰세용'],manual_parameters=[search], responses={200: 'Success'})
class SearchMarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    filter_backends = [SearchFilter] # filters에 SearchFilter 지정
    search_fields = ['store_name',]

class SearchByMarketLocationSi(APIView):
    @swagger_auto_schema(tags=['아직 사용 X'], responses={200: 'Success'})
    def get(self, request):
        address_si = request.GET.get("address_si")
        markets = Market.objects.filter(store_address_si = address_si)
        market_serializer = MarketSerializer(markets, many=True)
        return Response(market_serializer.data, status=200)
    
class SearchByMarketLocationGu(APIView):
    address_gu = openapi.Parameter('address_gu', openapi.IN_QUERY, description='address_gu', required=True, type=openapi.TYPE_STRING)
    @swagger_auto_schema(tags=['마켓을 구 단위로 구분해서 리스트로 보내는 기능'],manual_parameters=[address_gu], responses={200: 'Success'})
    def get(self, request):
        address_gu = request.GET.get("address_gu")
        markets = Market.objects.filter(store_address_gu = address_gu)
        market_serializer = MarketSerializer(markets, many=True)
        return Response(market_serializer.data, status=200)
    

class CheckIsLike(APIView):
    def get(self, request):
        store_id = request.GET.get("store_id")
        market = Market.objects.get(store_id=store_id)
        if request.user in market.store_like_people.all():
            return Response({'message': True}, status=200)
        else:
            return Response({'message': False}, status=200)

class MyLikeList(APIView):
    def get(self, request):
        market_list = request.user.like_table.all()
        market_serializer = MarketSerializer(market_list, many=True)
        return Response(market_serializer.data, status=200)
    
class MyOrderList(APIView):
    def get(self, request):
        order_detail_list = request.user.order_details.all()
        order_detail_serializer = OrderDetailSerializer(order_detail_list,many=True)
        return Response(order_detail_serializer.data, status = 200)
    
class MyDesignCakeList(APIView):
    def get(self, request):
        my_design_cake_list = request.user.my_cakes.all()
        my_cake_serializer = MyCakeSerializer(my_design_cake_list, many=True)
        return Response(my_cake_serializer.data, status=200)
