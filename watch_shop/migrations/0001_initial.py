# Generated by Django 4.1.6 on 2023-02-08 17:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Belts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=100, verbose_name='Материал ремешка')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название производителя')),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('material', models.CharField(max_length=250, verbose_name='Материал корпуса')),
                ('price', models.IntegerField(null=True, verbose_name='Цена')),
                ('warranty', models.IntegerField(null=True, verbose_name='Гарантия')),
                ('is_water_resist', models.BooleanField(null=True, verbose_name='Водостойкие')),
                ('gender', models.CharField(max_length=100, verbose_name='Пол')),
                ('diameter', models.IntegerField(null=True, verbose_name='Диаметр')),
                ('thickness', models.IntegerField(null=True, verbose_name='Толщина')),
                ('belt_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='watch_shop.belts', verbose_name='Материал ремешка')),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='watch_shop.manufacturer', verbose_name='Производитель')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон для связи')),
                ('status', models.CharField(max_length=100, verbose_name='Статус заказа')),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('ready_time', models.DateTimeField(default=datetime.datetime(2023, 2, 15, 21, 19, 32, 734177))),
                ('price', models.IntegerField(null=True, verbose_name='Цена заказа')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch_shop.watch', verbose_name='Заказ')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch_shop.watch', verbose_name='Товар в корзине')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
