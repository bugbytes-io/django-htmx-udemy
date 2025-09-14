from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete-book/<int:pk>/', views.delete_book, name='delete-book'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('search/', views.search_books, name='search')
]
