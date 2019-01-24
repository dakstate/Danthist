from django.contrib import admin
from .models import client, content, servers, doctor, user, Visit, Log

# Register your models here.
admin.site.register(client)
admin.site.register(content)
admin.site.register(servers)
admin.site.register(doctor)
admin.site.register(user)
admin.site.register(Visit)
admin.site.register(Log)
