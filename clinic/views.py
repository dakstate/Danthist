from django.shortcuts import HttpResponse, render
from .models import servers, content

def index(request):
    main = servers.objects.all()
    news = content.objects.all()
    return render(request,'clinic/index.html',{'context':main},{'news':news})

def register(request):
    return render(request,'clinic/register.html')
