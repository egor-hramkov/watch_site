from django.urls import path

from watch_shop.views import mainpage, watches_list, get_watch, register, auth

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('watches', watches_list, name='watches'),
    path('watches/<int:pk>', get_watch, name='get_watch'),
    path('registration/', register, name='registration'),
    path('auth/', auth, name='auth'),
]