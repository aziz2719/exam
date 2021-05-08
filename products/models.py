from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, models.SET_NULL, 'category_product', null=True)
    name = models.CharField('Название', max_length=255)
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')
    image = models.FileField('Фото', upload_to='product_images/')
    good_quantity = models.PositiveSmallIntegerField('Количество товара', default=1) 


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}'