from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from clinic.models import user, user
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewUser

@csrf_protect
def index(request):
	date = {}
	#if not request.user.is_authenticated:
	#	return HttpResponseRedirect('/lk/login/')
	if request.session['user'] == "dell":
		return HttpResponseRedirect('/lk/login/')
	else:
		us =  user.objects.get(id = request.session['user'])
		date['Type'] = us.Type
		date['Fam'] = us.Fam
		date['Im'] = us.Im
		date['Otch'] = us.Otch
		print(us.Type)
		return render(request,'adminbar/index.html', {'date' : date})




@csrf_protect
def login(request):
	date = {}
	if request.session['user'] != "dell":
		return HttpResponseRedirect('/lk/')
	if request.POST:
		Tel = request.POST.get('username', '')
		Passw = request.POST.get('password', '')
		try:
			us =  user.objects.get(Numm = Tel, Passw = Passw)
			request.session['user'] = us.id
			return HttpResponseRedirect('/lk/')
		except ObjectDoesNotExist:
			date['login_error'] = "Пользователь не найден!"
			return render(request, 'adminbar/login.html', date)

	return render(request,'adminbar/login.html')

def logout(request):
	try:
		request.session['user'] = "dell"
	except KeyError:
		pass
	return HttpResponseRedirect('/lk/login/')


def updall(request):
	date = {}
	if request.session['user'] == "dell":
		return HttpResponseRedirect('/lk/login/')
	else:
		us =  user.objects.get(id = request.session['user'])
		date['Type'] = us.Type
		date['Fam'] = us.Fam
		date['Im'] = us.Im
		date['Otch'] = us.Otch
		print(us.Ty[0][1])
		red = user.objects.all()
		return render(request,'adminbar/udall.html', {'date' : date, 'pul': red})

# def add(request):
# 	date = {}
# 	if request.session['user'] == "dell":
# 		return HttpResponseRedirect('/lk/login/')
# 	else:
# 		us =  user.objects.get(id = request.session['user'])
# 		date['Type'] = us.Type
# 		date['Fam'] = us.Fam
# 		date['Im'] = us.Im
# 		date['Otch'] = us.Otch
# 		return render(request,'adminbar/docadd.html', {'date' : date})

def add(request):
		form = NewUser()
		if request.method == 'POST':
			form = NewUser(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/lk/')
             # form.update(csrf(request))
		else:
			form = NewUser()
			return render(request,'adminbar/docadd.html', {'form': form})
