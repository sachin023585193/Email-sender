
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('iamadmin/', admin.site.urls),
    path('',include('EmailApp.urls')),
]
