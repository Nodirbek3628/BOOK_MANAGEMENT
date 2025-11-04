from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpRequest

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request=request,template_name='home.html')

def about_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('About ')