from django import forms
from clinic.models import user

class NewUser(forms.ModelForm):

    class Meta:
        model = user
        fields = ('Fam', 'Im','Otch', 'Numm', 'Dolj', 'Passw')
