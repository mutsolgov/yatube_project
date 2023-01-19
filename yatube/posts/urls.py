# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # Страница с п
    path('posts/', views.group_posts),
]