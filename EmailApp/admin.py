from django.contrib import admin
from .models import SecretKey

class SecretKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'email', 'projectname')
    search_fields = ('key', 'email', 'projectname')
# Register your models here.
admin.site.register(SecretKey,SecretKeyAdmin)