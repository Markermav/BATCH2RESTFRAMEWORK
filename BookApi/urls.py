from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.get_all_books, name='get_all_books'),
    path('book/<int:pk>', views.getBook, name='getBook'),
    path('create', views.createBook, name='createBook'),
    path('update/<int:id>', views.updateBook, name='updateBook'),





]
