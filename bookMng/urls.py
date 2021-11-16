from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('all_books', views.all_books, name='all_books'),
    path('my_books', views.my_books, name='my_books'),
    path('post_book', views.post_book, name='post_book'),
    path('search_books', views.search_books, name='search_books'),
    path('about_us', views.about_us, name='about_us'),
    path('book_details/<int:book_id>', views.book_details, name='book_details'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete')
]