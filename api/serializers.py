from .models import Product, Kit, KitProducts
from rest_framework import serializers

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'sku', 'cost', 'price', 'stock')

class KitProductsSerializers(serializers.ModelSerializer):

    class Meta:
        model = KitProducts
        fields = ('id','sku', 'quantity', 'discount')

class KitSerializers(serializers.ModelSerializer):
    products = KitProductsSerializers(many=True)
    class Meta:
        model = Kit
        fields = ('id', 'kit_name', 'kit_sku', 'products')