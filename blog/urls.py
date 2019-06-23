from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"),
    path('write', views.write, name="write"),
    path('create', views.create, name="create")
]
