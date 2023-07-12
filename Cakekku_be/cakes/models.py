from django.db import models
from markets.models import Market
from random import choice
import os
from uuid import uuid4
from django.utils import timezone
from accounts.models import User

class Cake(models.Model):
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


class OrderDetail(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_level = models.IntegerField(verbose_name="예약 진행 단계")
    order_user = models.ForeignKey(to=User,verbose_name="예약 유저")
    order_cake = models.ManyToManyField(to=Cake,on_delete=models.CASCADE,verbose_name="예약한 케이크")
    
    