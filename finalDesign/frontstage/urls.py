from django.urls import path, re_path
from . import views

urlpatterns = [
    path('menuInfo', views.menuInfo),
    path('foodInfo', views.foodInfo),
    path('orderinfo', views.orderinfo),
    path('createorder/', views.createorder),
    path('getOrderInfo', views.getOrderInfo),
    path('getOrder', views.getOrder),
    path('qsearch', views.qsearch),
    path('login/', views.login),
    path('sign/', views.sign),
    path('updatalogin', views.updatalogin),
]