from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),

    path('getkey/',views.getkey,name='getkey'),
    path('mailto/<email>/',views.mailtoemail,name='mailto'),
    path('key/<key>/',views.mailtokey,name='key'),

    path('submitted/',views.submitted,name='submitted'),
]