from django.shortcuts import render
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Market, Review
from .serializers import MarketSerializer, ReviewSerializer
from rest_framework.filters import SearchFilter
from rest_framework import viewsets


class MarketListAPIView(APIView):
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

class MarketRetrieveAPIView(RetrieveAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class MarketLike(APIView):
    def post(self, request):
        market = Market.objects.get(store_id = request.data["store_id"])
        if request.user in market.store_like_people.all():
            market.store_like_people.remove(request.user)
        else:
            market.store_like_people.add(request.user)
        return Response({"message":market.store_like_people.count()})
    

class ReviewCreateAPIView(APIView):
    def post(self, request):
        review = Review()
        review.review_image1 = request.data.get("review_image1")
        review.review_image2 = request.data.get("review_image2")
        review.review_image3 = request.data.get("review_image3")
        review.review_image4 = request.data.get("review_image4")
        review.review_image5 = request.data.get("review_image5")
        review.review_content = request.data.get("review_content")
        review.review_market = Market.objects.get(store_id = request.data.get("review_market"))
        review.review_tag1 = request.data.get("review_tag1")
        review.review_tag2 = request.data.get("review_tag2")
        review.review_tag3 = request.data.get("review_tag3")
        review.review_tag4 = request.data.get("review_tag4")
        review.review_tag5 = request.data.get("review_tag5")
        review.review_tag6 = request.data.get("review_tag6")
        review.review_score = request.data.get("review_score")
        review.save()

        reviewed_market = Market.objects.get(store_id=request.data["review_market"])
        total_sum =0
        count =0
        average =0
        for reviewByMarket in reviewed_market.reviews.all():
            total_sum += reviewByMarket.review_score
            count += 1
        if count!=0:
            average = total_sum/count
        reviewed_market.store_average_score = average
        reviewed_market.save()

        review_serializer = ReviewSerializer(reviewByMarket)
        return Response(review_serializer.data, status=200)
    
class MyReviewList(APIView):
    def get(self, request):
        reviews = Review.objects.filter(review_writer = request.user)
        review_serializer = ReviewSerializer(reviews, many=True)
        return Response(review_serializer.data, status=200)
        


class SearchMarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    filter_backends = [SearchFilter] # filters에 SearchFilter 지정
    search_fields = ['store_name',]
