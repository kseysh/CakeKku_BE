from .models import *
from rest_framework import serializers

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class MyCakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCake
        fields = '__all__'

class CakeAdditionalOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = [
            'store_cake_size1',
            'store_cake_size2',
            'store_cake_size3',
            'store_cake_size4',
            'store_cake_size5',
            'store_bread_sanding1',
            'store_bread_sanding2',
            'store_bread_sanding3',
            'store_bread_sanding4',
            'store_bread_sanding5',
        ]
        depth = 1


