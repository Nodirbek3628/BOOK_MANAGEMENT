from django.urls import path
from .views import home_view, books_view,books_detail_view


app_name = "books"

urlpatterns = [
    path('',home_view,name='home_pages'),
    path('books/',books_view,name='books_pages'),
    path('books/<int:book_id>',books_detail_view, name='detail')
]