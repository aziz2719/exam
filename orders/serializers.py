from rest_framework import serializers
from .models import Order, OrderProduct

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'product', 'order', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    product_order_product = OrderProductSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'date', 'total_price', 'address', 'status', 'product_order_product')
        



        
    """def create(self, validated_data):
        products = validated_data.pop('product_order_product')
        order = Order.objects.create(**validated_data)
        for product in products:
            product_order = OrderProduct.objects.create(**product)
            product_order.order = order
            product_order.save()
        order.set_total_quantity()
        return order"""