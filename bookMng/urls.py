from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all_books', views.all_books, name='all_books'),
    path('search_books', views.search_books, name='search_books'),
    path('post_book', views.post_book, name='post_book'),
    path('faq', views.faq, name='faq'),
    path('about_us', views.about_us, name='about_us'),
    path('book_details/<int:book_id>', views.book_details, name='book_details'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('my_books', views.my_books, name='my_books'),
    path('messagebox/incoming', views.incoming_messages, name='incoming_messages'),
    path('messagebox/outgoing', views.outgoing_messages, name='outgoing_messages'),
    path('messagebox/compose', views.compose_message, name='compose_message'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('add_to_cart/<int:book_id>', views.add_to_cart, name=''),
    path('remove_from_cart/<int:book_id>', views.remove_from_cart, name=''),
    path('wish_list/', views.wish_list, name='shopping_cart'),
    path('add_to_wish_list/<int:book_id>', views.add_to_wish_list, name=''),
    path('remove_from_wish_list/<int:book_id>', views.remove_from_wish_list, name='')
]