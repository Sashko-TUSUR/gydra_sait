from django.db import models


class User(models.Model):
    # email
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    birthday = models.DateField("Дата рождения")
    address = models.CharField("Адрес", max_length=100)
    cost_orders = models.FloatField("Сумма покупок")
    count_orders = models.IntegerField("Количество заказов")
    count_rejects = models.IntegerField("Количество отказов")
    percent_buy = models.FloatField("Процент выкупа")

    def __str__(self):
        return self.name


class Orders(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    count_orders = models.IntegerField('Количество заказов')
    cost = models.FloatField("Стоимость")
    address_delivery = models.CharField("Адрес доставку", max_length=100)
    date_order = models.DateField("Дата заказа")
    date_delivery = models.DateField("Дата доставки")
    status = models.BooleanField("Статус")

    def __str__(self):
        return self.cost


class StatusesOrders(models.Model):
    status = models.CharField('Статус', max_length=100)

    def __str__(self):
        return self.status


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


class Basket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id
