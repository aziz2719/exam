from rest_framework import serializers

from products.models import Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_product = ProductCategorySerializer(read_only=True, many=True)
    
    class Meta:
        model = Product
        fields = ('category', 'name', 'price', 'description', 'image', 'good_quantity', 'category_product')