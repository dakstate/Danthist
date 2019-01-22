from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.



def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('/lk/login/')
	return render(request,'adminbar/index.html')


def login(request):
	return render(request,'adminbar/login.html')