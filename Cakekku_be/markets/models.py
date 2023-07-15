from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
from django.utils import timezone

class CakeSize(models.Model):
    cake_size_id = models.AutoField(primary_key=True)
    cake_size_name = models.CharField(verbose_name="케이크 사이즈 이름",max_length=20,default="케이크 사이즈 이름")
    cake_size_plate = models.CharField(verbose_name="몇 인분인지",max_length=10,default=1)
    cake_size_cm = models.IntegerField(verbose_name="케이크 cm",default=0)
    price = models.IntegerField(verbose_name="케이크 사이즈 시작 가격",default=0)
    is_extra_content = models.BooleanField(verbose_name="extra content인지",default=False)
    extra_content = models.TextField(verbose_name="extra content",default="콘텐트를 입력해주세요.")
    def __str__(self):
        return self.cake_size_name
class BreadSanding(models.Model):
    bread_sanding_id = models.AutoField(primary_key=True)
    bread_sanding_content = models.CharField(verbose_name="빵 + 샌딩",default="기본 빵 + 기본 샌딩",max_length=20)
    price = models.IntegerField(verbose_name="빵 + 샌딩 가격",default=0)
    is_additional_option = models.BooleanField(verbose_name="추가 옵션인지", default=False)
    additional_option = models.CharField(verbose_name="추가 옵션",default="추가 옵션",max_length=20)
    def __str__(self):
        return self.bread_sanding_content

class Market(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(verbose_name="가게 이름",max_length=20)
    store_address = models.CharField(verbose_name="가게 주소", max_length=30,blank=True,null=True)
    store_address_si = models.CharField(verbose_name="가게 주소-시", max_length=10,blank=True,null=True)
    store_address_gu = models.CharField(verbose_name="가게 주소-구", max_length=10,blank=True,null=True)
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
    store_menu_content1 = models.TextField(verbose_name="메뉴 글 1",default="메뉴 소개글을 작성해주세요.")
    store_menu_content2 = models.TextField(verbose_name="메뉴 글 2",default="메뉴 소개글을 작성해주세요.")
    store_menu_content3 = models.TextField(verbose_name="메뉴 글 3",default="메뉴 소개글을 작성해주세요.")
    store_order_form_content1 = models.TextField(verbose_name="주문 양식 글 1",default="주문 양식 소개글을 작성해주세요.")
    store_order_form_content2 = models.TextField(verbose_name="주문 양식 글 2",default="주문 양식 소개글을 작성해주세요.")
    store_order_form_content3 = models.TextField(verbose_name="주문 양식 글 3",default="주문 양식 소개글을 작성해주세요.")
    store_cake_size1 = models.ForeignKey(to=CakeSize,verbose_name="케이크 사이즈 1",on_delete=models.CASCADE,null=True,blank=True,related_name="cake_size_set_1")
    store_cake_size2 = models.ForeignKey(to=CakeSize,verbose_name="케이크 사이즈 2",on_delete=models.CASCADE,null=True,blank=True,related_name="cake_size_set_2")
    store_cake_size3 = models.ForeignKey(to=CakeSize,verbose_name="케이크 사이즈 3",on_delete=models.CASCADE,null=True,blank=True,related_name="cake_size_set_3")
    store_cake_size4 = models.ForeignKey(to=CakeSize,verbose_name="케이크 사이즈 4",on_delete=models.CASCADE,null=True,blank=True,related_name="cake_size_set_4")
    store_cake_size5 = models.ForeignKey(to=CakeSize,verbose_name="케이크 사이즈 5",on_delete=models.CASCADE,null=True,blank=True,related_name="cake_size_set_5")
    store_bread_sanding1 = models.ForeignKey(to=BreadSanding,verbose_name="빵 샌딩 선택 1",on_delete=models.CASCADE,null=True,blank=True,related_name="bread_sanding_set_1")
    store_bread_sanding2 = models.ForeignKey(to=BreadSanding,verbose_name="빵 샌딩 선택 2",on_delete=models.CASCADE,null=True,blank=True,related_name="bread_sanding_set_2")
    store_bread_sanding3 = models.ForeignKey(to=BreadSanding,verbose_name="빵 샌딩 선택 3",on_delete=models.CASCADE,null=True,blank=True,related_name="bread_sanding_set_3")
    store_bread_sanding4 = models.ForeignKey(to=BreadSanding,verbose_name="빵 샌딩 선택 4",on_delete=models.CASCADE,null=True,blank=True,related_name="bread_sanding_set_4")
    store_bread_sanding5 = models.ForeignKey(to=BreadSanding,verbose_name="빵 샌딩 선택 5",on_delete=models.CASCADE,null=True,blank=True,related_name="bread_sanding_set_5")



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
    review_writer = models.ForeignKey(to=User,verbose_name="리뷰 작성자",null=True,on_delete=models.CASCADE)




    