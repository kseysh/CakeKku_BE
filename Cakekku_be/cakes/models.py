from django.db import models

class Cake(models.Model):
    cake_id = models.AutoField(primary_key=True)

class OrderDetail(models.Model):
    order_id = models.AutoField(primary_key=True)
