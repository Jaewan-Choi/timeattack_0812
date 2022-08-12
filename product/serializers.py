from rest_framework import serializers
from .models import Product, ProductStatus


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProductStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductStatus
        fields = "__all__"