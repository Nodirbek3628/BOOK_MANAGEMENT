from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpRequest

books = [
{

    'id':1,
    'name': 'O\'tgan Kunlar',
    'author': 'Abdulla Qodiriy'
},
{
    'id':2,
    'name': 'Dost ortirish',
    'author': 'Deyl Karnegi'
},
{
    'id':3,
    'name': 'Atom odatlari',
    'author': 'stev jops'
},
{
    'id':4,
    'name': 'Xamsa',
    'author': 'Navoiy'
}]

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request=request,template_name='home.html')

def books_view(request: HttpRequest) -> HttpResponse:
    context = {
        'books':books,
        'name': 'Ali'
    }

    return render(request=request,context=context,template_name='books.html')


def books_detail_view(request: HttpRequest,book_id:int) -> HttpResponse:
    for book in books:
        if book['id'] == book_id:
            context = {
                'book':book
            }
            return render (request=request,template_name='book_detail.html',context=context)

    return render(request=request,template_name='books.html') 