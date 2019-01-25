from django import forms
from clinic.models import user, Visit
from django.forms import ModelForm
from django.contrib.admin import widgets

class NewUser(forms.ModelForm):

    class Meta:
        model = user
        fields = ('Fam', 'Im','Otch', 'Numm', 'Dolj', 'Passw')


class NV(ModelForm):
	class Meta:
		model = Visit
		fields = ('date', 'Numm')
	def __init__(self, *args, **kwargs):
		super(NV, self).__init__(*args, **kwargs)
		self.fields['date'].widget = widgets.AdminSplitDateTime()