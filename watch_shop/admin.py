from django.contrib import admin
from .models import *


class WatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price', 'warranty', 'is_water_resist', 'gender')
    list_display_links = ('name', 'manufacturer', 'price', 'gender')
    search_fields = ('name', 'manufacturer')
    list_filter = ('name', 'manufacturer', 'price',)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'address', 'phone', 'status', 'order_time', 'ready_time', 'price')
    list_display_links = ('user', 'order', 'address', 'phone', 'status', 'order_time', 'ready_time', 'price')
    search_fields = ('address', 'phone')
    list_filter = ('user', 'order', 'address', 'phone', 'status', 'order_time', 'ready_time', 'price')


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Watch, WatchAdmin)
admin.site.register(Basket, )
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Belts, )
