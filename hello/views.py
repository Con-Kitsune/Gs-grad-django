from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    data = News.objects.all()
    params = {
            'data': data,
            }
    return render(request, 'hello/index.html', params)

def call(request):
    params = {
            'msg': 'コードを共有してください。',
            }
    return render(request, 'hello/call.html', params)
# Create your views here.
