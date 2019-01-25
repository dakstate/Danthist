from django.urls import path
from . import views


urlpatterns = [
       path('', views.index),
       path('login/', views.login),
       path('logout/', views.logout),
       path('user/upd/', views.updall),
       path('user/add/', views.add),
]
