from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from clinic.models import user
from django.core.exceptions import ObjectDoesNotExist

@csrf_protect
def index(request):
	#if not request.user.is_authenticated:
	#	return HttpResponseRedirect('/lk/login/')
	if request.session['user'] == "dell":
		return HttpResponseRedirect('/lk/login/')
	else:
		return render(request,'adminbar/index.html')




@csrf_protect
def login(request):
#
	if request.session['user'] != "dell":
		return HttpResponseRedirect('/lk/')
	if request.POST:
		Fam = request.POST.get('username', '')
		Passw = request.POST.get('password', '')
		try:
			us =  user.objects.get(Fam = Fam, Passw = Passw)
			request.session['user'] = us.id
			return HttpResponseRedirect('/lk/')
		except ObjectDoesNotExist:
			return HttpResponseRedirect('/')

	return render(request,'adminbar/login.html')

def logout(request):
	try:
		request.session['user'] = "dell"
	except KeyError:
		pass
	return HttpResponseRedirect('/lk/login/')