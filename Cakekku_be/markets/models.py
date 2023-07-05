from django.db import models
from django.contrib.auth.models import User
from cakes.models import OrderDetail
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
    store_like = models.ManyToManyField(to=User,blank=True, related_name="like_table")
    store_hashtag_1 = models.CharField(verbose_name="hashtag_1",default="입체 케이크", max_length=20)
    store_hashtag_2 = models.CharField(verbose_name="hashtag_2",default="캐릭터 케이크", max_length=20) 

    def __str__(self):
        return self.store_name

class Review(models.Model):
    review_order_detail = models.ForeignKey(to=OrderDetail,on_delete=models.CASCADE)
    review_id = models.AutoField(primary_key=True)
    review_image = models.ImageField(verbose_name="리뷰 이미지",blank=True,null=True,upload_to="./image")
    review_score = models.IntegerField(verbose_name="별점")
    review_content = models.TextField(verbose_name="리뷰 내용",blank=True)
    # review_hashtag = 
    review_market = models.ForeignKey(to=Market,blank=True,null=True,on_delete=models.CASCADE,verbose_name="리뷰한 가게")
    review_lower_price = models.IntegerField(verbose_name="최저 가격",blank=True)
    review_higher_price = models.IntegerField(verbose_name="최고 가격",blank=True)
