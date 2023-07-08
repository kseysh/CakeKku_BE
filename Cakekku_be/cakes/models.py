from django.db import models
from markets.models import Market

class Cake(models.Model):
    cake_id = models.AutoField(primary_key=True)
    cake_price = models.IntegerField(verbose_name="케이크 가격",null=True,blank=True)
    cake_market = models.ForeignKey(Market,verbose_name="케이크 마켓",on_delete=models.CASCADE,related_name="cakes",null=True,blank=True)