from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('', include('basics.urls')),
    path('', include('hlApp.urls')),
    path('admin/', admin.site.urls),
]
