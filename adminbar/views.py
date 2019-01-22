from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect



def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('/lk/login/')
	return render(request,'adminbar/index.html')



@csrf_protect
def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/lk/')
	return render(request,'adminbar/login.html')