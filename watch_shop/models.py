from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User


class Watch(models.Model):
    """Часы"""
    name = models.CharField(max_length=100, verbose_name="Название")
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE, null=True, verbose_name='Производитель')
    material = models.CharField(max_length=250, verbose_name="Материал корпуса")
    belt_type = models.ForeignKey("Belts", on_delete=models.CASCADE, null=True, verbose_name='Материал ремешка')
    price = models.IntegerField(null=True, verbose_name="Цена")
    warranty = models.IntegerField(null=True, verbose_name="Гарантия")
    is_water_resist = models.BooleanField(null=True, verbose_name="Водостойкие")
    gender = models.CharField(max_length=100, verbose_name="Пол")
    diameter = models.IntegerField(null=True, verbose_name="Диаметр")
    thickness = models.IntegerField(null=True, verbose_name="Толщина")


class Basket(models.Model):
    """Корзина"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    product = models.ForeignKey("Watch", verbose_name="Товар в корзине", on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name="Количество")


class Orders(models.Model):
    """Заказы"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    order = models.ForeignKey("Watch", verbose_name="Заказ", on_delete=models.CASCADE)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=100, verbose_name="Телефон для связи")
    status = models.CharField(max_length=100, verbose_name='Статус заказа')
    order_time = models.DateTimeField(auto_now_add=True)
    ready_time = models.DateTimeField(default=datetime.now()+timedelta(days=7))
    price = models.IntegerField(null=True, verbose_name="Цена заказа")


class Manufacturer(models.Model):
    """Производители"""
    name = models.CharField(max_length=100, verbose_name="Название производителя")


class Belts(models.Model):
    """Типы ремешков"""
    material = models.CharField(max_length=100, verbose_name="Материал ремешка")
