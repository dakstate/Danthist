from django.contrib import admin
from .models import client, content, servers, doctor



admin.site.register(client)
admin.site.register(content)
admin.site.register(servers)
admin.site.register(doctor)
# Register your models here.
