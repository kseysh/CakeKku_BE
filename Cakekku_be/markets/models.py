from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
from django.utils import timezone


class Market(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(verbose_name="가게 이름",max_length=20)
    store_address = models.CharField(verbose_name="가게 주소", max_length=50)
    def upload_to_func(instance,filename):
        prefix = timezone.now().strftime("%Y/%m/%d")
        file_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()
        return "/".join(
            [prefix, file_name, extension,]
        )
    store_thumbnail_image = models.ImageField(verbose_name="가게 대표 이미지",blank=True,upload_to=upload_to_func)
    store_like_people = models.ManyToManyField(User,blank=True, related_name="like_table")
    # 좋아요 수로 바꿔주기
    store_hashtag_1 = models.CharField(verbose_name="hashtag_1",default="입체 케이크", max_length=20)
    store_hashtag_2 = models.CharField(verbose_name="hashtag_2",default="캐릭터 케이크", max_length=20)
    
    # store_score= models.IntegerField(verbose_name="가게 별점")
    # store_lower_price = models.IntegerField(verbose_name="가게 최저 가격")
    # store_higher_price = models.IntegerField(verbose_name="가게 최고 가격")
    # store_review_count = models.IntegerField(verbose_name="가게 리뷰 수")


    def __str__(self):
        return self.store_name

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_image = models.ImageField(verbose_name="리뷰 이미지",blank=True,null=True,upload_to="./image")
    review_score = models.IntegerField(verbose_name="별점")
    review_content = models.TextField(verbose_name="리뷰 내용",blank=True)
    review_market = models.ForeignKey(to=Market,blank=True,null=True,on_delete=models.CASCADE,verbose_name="리뷰한 가게",related_name="reviews")
    