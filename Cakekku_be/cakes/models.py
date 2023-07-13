from django.db import models
from markets.models import Market
from random import choice
import os
from uuid import uuid4
from django.utils import timezone
from django.contrib.auth.models import User
class Cake(models.Model): # 마켓에 display될 케이크
    cake_id = models.AutoField(primary_key=True)
    cake_price = models.IntegerField(verbose_name="케이크 가격",null=True,blank=True)
    cake_market = models.ForeignKey(Market,verbose_name="케이크 마켓",on_delete=models.CASCADE,related_name="cakes",null=True,blank=True)
    cake_shape = models.IntegerField(verbose_name="케이크 모양",null=True,blank=True)

    def upload_to_func(instance,filename):
        prefix = timezone.now().strftime("%Y/%m/%d")
        file_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()
        return "/".join(
            [prefix, file_name, extension,]
        )
    cake_image = models.ImageField(verbose_name="케이크 이미지",null=True,blank=True,upload_to=upload_to_func)

class MyCake(models.Model):
    my_cake_id =  models.AutoField(primary_key=True)
    def upload_to_func(instance,filename):
        prefix = timezone.now().strftime("%Y/%m/%d")
        file_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()
        return "/".join(
            [prefix, file_name, extension,]
        )
    my_cake_image = models.ImageField(verbose_name="케이크 이미지",null=True,blank=True,upload_to=upload_to_func)
    my_cake_user = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="my_cakes",null=True)



class AdditionalOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    option_price = models.IntegerField(default=0,verbose_name="추가 옵션 가격")
    option_name = models.CharField(max_length=20,verbose_name="추가 옵션 이름")

class OrderDetail(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_stage = models.IntegerField(verbose_name="주문 단계",default=0)
    order_user = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="예약 유저",related_name="order_details")
    order_cake = models.ManyToManyField(to=Cake,verbose_name="예약 케이크",blank=True)
    order_additional_option = models.ForeignKey(to=AdditionalOption, verbose_name="추가 옵션",on_delete=models.CASCADE,null=True,blank=True)
    order_final_price = models.IntegerField(default=0,verbose_name="추가 옵션 가격")
    is_pickup_complete = models.BooleanField(default=False,verbose_name="픽업 완료 유무")

class OrderDetailByMyCake(models.Model):
    my_order_id = models.AutoField(primary_key=True)
    order_stage = models.IntegerField(verbose_name="주문 단계",default=0)
    order_user = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="예약 유저",related_name="my_order_details")
    order_cake = models.ManyToManyField(to=MyCake,verbose_name="예약 케이크",blank=True)
    order_additional_option = models.ForeignKey(to=AdditionalOption, verbose_name="추가 옵션",on_delete=models.CASCADE,null=True,blank=True)
    order_final_price = models.IntegerField(default=0,verbose_name="추가 옵션 가격")
    is_pickup_complete = models.BooleanField(default=False,verbose_name="픽업 완료 유무")
