"""login_app urlpatterns"""
from django.urls import path
from django.conf.urls import include
from two_factor.urls import urlpatterns as tf_urls
from . import views


app_name = 'login_app'

urlpatterns = [
    #path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('', include(tf_urls)),
]
