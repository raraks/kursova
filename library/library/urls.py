# library/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/books', views.get_books, name='get_books'),
    path('add-book', views.add_book, name='add_book'),
    path('book/<int:book_id>', views.book_detail, name='book_detail'),
    path('admin/', admin.site.urls),
]