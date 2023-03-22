from django.shortcuts import render, redirect
from datetime import date
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpRequest, HttpResponse
from .smtplib import ContactForm

# Create your views here.
def index(req):
    todayYear = date.today().year
    return render(req,'index.html', {'year':todayYear})

def about(req):
    return render(req,'about.html', {})

def events(req):
    return render(req,'events.html', {})

def bylaw(req):
    return render(req,'bylaw.html', {})

def contact(req):
    if req.method == 'GET':
        return render(req,'contact.html', {})
    else:
        form = ContactForm(req.POST,req.FILES)
        print(f'form {form}')
        if form.is_valid():
            fromemail = req.POST.get('email',False)
           
            body  = {
                'name' : 'Name: ' + req.POST.get('name',False) + ',',
                'message' : 'Message: ' + req.POST.get('message',False),  
                'email' : 'From: ' + fromemail,                               
            }
                  
            subject = req.POST.get('subject',False)
            message = "\n".join(body.values())
            try:
                send_mail(subject,message,fromemail,['egizaw926@gmail.com'],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("index")
        #form = ContactForm()           
        return render(req,'contact.html', {'name':fromemail})

def login(req):
    return render(req,'login.html', {})

def doctrinal(req):
    return render(req,'doctrinal.html',{})

def spritual(req):
    return render(req, 'spritual.html',{})

def bibleStudy(req):
    return render(req, 'bible.html',{})
