
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lk/', include('adminbar.urls')),
    path('', include('clinic.urls')),
]
