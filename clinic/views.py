from django.shortcuts import HttpResponse, render
from .models import servers, content, user

def index(request):
    main = servers.objects.all()
    news = content.objects.all()
    us = user.objects.filter(Type = 'V')
    return render(request,'clinic/index.html',{'context':main, 'news':news, 'us':us})

def register(request):
    return render(request,'clinic/register.html')
