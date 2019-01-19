from django.contrib import admin
<<<<<<< HEAD
from .models import client
<<<<<<< HEAD
=======
=======
from .models import client, content, servers, doctor
>>>>>>> 82b7bd57d678ff0788822ce6441d076910f773a1



admin.site.register(client)
<<<<<<< HEAD
>>>>>>> 630afdcf4ba23dbc3489a3f312a40274acf2793e
=======
admin.site.register(content)
admin.site.register(servers)
admin.site.register(doctor)
>>>>>>> 82b7bd57d678ff0788822ce6441d076910f773a1
# Register your models here.

admin.site.register(client)
