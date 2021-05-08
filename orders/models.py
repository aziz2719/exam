from django.db import models
from products.models import Product
from django.db.models import F, Sum


class Order(models.Model):
    CHOICES = (
        ('N','New courier appointed'),#новый курьер назначен
        ('T','The manager looked at the order and appointed a courier'),#менеджер посмотрел заказ и назнач нов курьера
        ('O','On my way'),#в пути
        ('D','Delivered'),#доставлено
        ('С','Сanceled'),#отменен
    )
    customer = models.ForeignKey('users.User', models.SET_NULL, related_name='customer_order', null=True)
    date = models.DateTimeField('Дата заказа', auto_now_add=True)
    total_price = models.DecimalField('Цена', max_digits=10, decimal_places=0, default=0, blank=True, null=True)
    address = models.CharField('Адрес доставки', max_length=255)
    status = models.CharField(max_length=100, choices=CHOICES)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return self.address
    

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, 'product_order', null=True)
    order = models.ForeignKey(Order, models.CASCADE, related_name='product_order_product', null=True)
    quantity = models.PositiveSmallIntegerField('Количество товара', default=1) 

    class Meta:
        verbose_name = 'Заказ продукта'
        verbose_name_plural = 'Заказ продуктов'

    """def set_total_quantity(self):
        if self.product__good_quantity < quantity or self.product__good_quantity == 0:
            print('В таком количестве товара не имеется, укажите меньше')
        else:
            self.product__good_quantity = self.product_order_product.all().aggregate(product__good_quantity='product__good_quantity' - 'quantity')['product__good_quantity']
        print(80*'r')
        self.save()"""
