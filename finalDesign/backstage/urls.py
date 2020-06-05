from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.login),
    path('index', views.index),
    path('menu', views.menu),
    path('order1', views.order1),
    path('order2', views.order2),
    path('member', views.member),
    path('addmenu', views.addmenu),
    path('addmenu1', views.addmenu1),
    path('updatamenu', views.updatamenu),
    path('finish_updatamenu', views.finish_updatamenu),
    path('updataorder', views.updataorder),
    path('finish_upadataorder', views.finish_upadataorder),
    path('updatamember', views.updatamember),
    path('finishi_updatamember', views.finishi_updatamember),
    path('login2', views.login2),
    path('orderinfo', views.orderinfo),
    path('statistical', views.statistical),
]
