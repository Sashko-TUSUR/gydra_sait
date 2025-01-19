from django.db import models


# Create your models here.

class TypeProduct(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='type_products/', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Название товара", max_length=255)
    description = models.CharField('Описание', max_length=255, null=True, blank=True)
    type = models.ForeignKey(TypeProduct, on_delete=models.DO_NOTHING)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    count_storage = models.IntegerField("Количество на складе", null=True, blank=True)
    count_sells = models.IntegerField("Количество продаж", null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
