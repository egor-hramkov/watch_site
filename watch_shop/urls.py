from django.urls import path

from watch_shop.views import mainpage, watches_list, get_watch, register, auth, profile, \
    basket, add_to_basket, delete_from_basket, order_register, orders, logout_user

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('watches', watches_list, name='watches'),
    path('watches/<int:pk>', get_watch, name='get_watch'),
    path('registration/', register, name='registration'),
    path('auth/', auth, name='auth'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('basket/', basket, name='basket'),
    path('add_to_basket', add_to_basket, name='add_to_basket'),
    path('delete_from_basket/', delete_from_basket, name='delete_from_basket'),
    path('orders/', orders, name='orders'),
    #path('orders/<int:pk>', get_order, name='get_order'),
    path('order_register/', order_register, name='order_register'),
]
