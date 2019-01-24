from django.contrib import admin
from .models import client, content, servers, user, doctor, Visit, Log

# Register your models here.
admin.site.register(client)
admin.site.register(content)
admin.site.register(servers)
admin.site.register(user)
admin.site.register(Visit)
admin.site.register(Log)
admin.site.register(doctor)
