from django.http import HttpResponse, JsonResponse,response
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from .decorator import only_post
from .utils import GetEmailSubject
from .models import SecretKey

# Create your views here.
def home(request):
    # send_mail('test','This is test message',settings.EMAIL_HOST_USER,['sachin023585193@gmail.com'])
    return render(request,'EmailApp/home.html')

def getkey(request):
    if request.method == 'POST':
        print(request.POST)
        emails = request.POST['emails']
        project = request.POST['projectname']
        newkey = SecretKey.objects.create(email=emails,projectname=project)
        newkey.save()
        return JsonResponse({'key':newkey.key})
    return render(request,'EmailApp/getkey.html')

@only_post
def mailtoemail(request,email):
    form_fields = dict(request.POST).items()
    subject = GetEmailSubject(form_fields)
    send_mail('New Form Submitted',subject,settings.EMAIL_HOST_USER,[email])
    return redirect('submitted')

@only_post
def mailtokey(request,key):
    model = SecretKey.objects.get(key=key)
    form_fields = dict(request.POST).items()
    emails = model.email.split(',')
    subject = GetEmailSubject(form_fields)
    send_mail('New Form Submitted',subject,settings.EMAIL_HOST_USER,emails)
    return redirect('submitted')

def submitted(request):
    return render(request,'EmailApp/submitted.html')