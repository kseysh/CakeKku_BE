from django.db import models
from markets.models import Market
from random import choice
import string

class Cake(models.Model):
    cake_id = models.AutoField(primary_key=True)
    cake_price = models.IntegerField(verbose_name="케이크 가격",null=True,blank=True)
    cake_market = models.ForeignKey(Market,verbose_name="케이크 마켓",on_delete=models.CASCADE,related_name="cakes",null=True,blank=True)
    cake_shape = models.IntegerField(verbose_name="케이크 모양",null=True,blank=True)

    def user_path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
        arr = [choice(string.ascii_letters) for _ in range(8)]
        pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
        extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
        # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
        return '%s/%s.%s' % (instance.owner.username, pid, extension) # 예 : wayhome/abcdefgs.png
    cake_image = models.ImageField(verbose_name="케이크 이미지",null=True,blank=True,upload_to=user_path)