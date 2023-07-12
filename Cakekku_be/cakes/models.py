from django.db import models
from markets.models import Market
from random import choice
import os
from uuid import uuid4
from django.utils import timezone
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