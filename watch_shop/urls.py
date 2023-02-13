from django.urls import path

from watch_shop.views import mainpage, watches_list

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('watches', watches_list, name='watches'),
]