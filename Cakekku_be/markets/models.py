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
    
    store_average_score= models.DecimalField(verbose_name="가게 별점",default=0,null=True,max_digits=3,decimal_places=2)
    store_lower_price = models.IntegerField(verbose_name="가게 최저 가격",default=0)
    store_higher_price = models.IntegerField(verbose_name="가게 최고 가격",default=0)


    def __str__(self):
        return self.store_name

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    def upload_to_func(instance,filename):
        prefix = timezone.now().strftime("%Y/%m/%d")
        file_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()
        return "/".join(
            [prefix, file_name, extension,]
        )
    review_image1 = models.ImageField(verbose_name="리뷰 이미지 1",blank=True,null=True,upload_to=upload_to_func)
    review_image2 = models.ImageField(verbose_name="리뷰 이미지 2",blank=True,null=True,upload_to=upload_to_func)
    review_image3 = models.ImageField(verbose_name="리뷰 이미지 3",blank=True,null=True,upload_to=upload_to_func)
    review_image4 = models.ImageField(verbose_name="리뷰 이미지 4",blank=True,null=True,upload_to=upload_to_func)
    review_image5 = models.ImageField(verbose_name="리뷰 이미지 5",blank=True,null=True,upload_to=upload_to_func)
    review_score = models.IntegerField(verbose_name="별점",null=True)
    review_content = models.TextField(verbose_name="리뷰 내용",blank=True)
    review_market = models.ForeignKey(to=Market,blank=True,null=True,on_delete=models.CASCADE,verbose_name="리뷰한 가게",related_name="reviews")
    review_tag1 = models.BooleanField(verbose_name="#맛있어요",default=False)
    review_tag2 = models.BooleanField(verbose_name="#원하는디자인이에요",default=False)
    review_tag3 = models.BooleanField(verbose_name="#맞춤형디자인이에요",default=False)
    review_tag4 = models.BooleanField(verbose_name="#신선해요",default=False)
    review_tag5 = models.BooleanField(verbose_name="#친절해요",default=False)
    review_tag6 = models.BooleanField(verbose_name="#포장이꼼꼼해요",default=False)
    review_created_at = models.DateTimeField(verbose_name="리뷰 작성 시간",auto_now_add=True)



    