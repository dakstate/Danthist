from django.shortcuts import HttpResponse, render
from .models import servers, content, user
from django.views.decorators.csrf import csrf_protect
from adminbar.forms import NV  

def index(request):
    main = servers.objects.all()
    news = content.objects.all()
    us = user.objects.filter(Type = 'V')
    return render(request,'clinic/index.html',{'context':main, 'news':news, 'us':us})


@csrf_protect
def register(request, IdV):
	form = NV
	if request.POST:
		lol = request.POST.get('dat', 'vmvmjhb,b')
		return render(request, 'clinic/register.html', {'lol': lol, 'f1': form, 'id': IdV})

	return render(request,'clinic/register.html', {'f1': form, 'id': IdV})
