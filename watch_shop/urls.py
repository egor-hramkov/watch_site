from django.urls import path

from watch_shop.views import mainpage

urlpatterns = [
    path('', mainpage),
]