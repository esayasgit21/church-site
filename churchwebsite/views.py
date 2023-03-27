from django.shortcuts import render, redirect
from datetime import date
from django.core.mail import send_mail
from django.http import BadHeaderError, FileResponse, HttpRequest, HttpResponse
from .smtplib import ContactForm
import qrcode
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image
#import requests
#import urllib
# import matplotlib.font_manager as fm
# Create your views here.
def index(req):
    todayYear = date.today().year
    return render(req,'index.html', {'year':todayYear})

def about(req):
    return render(req,'about.html', {})

def events(req):
    return render(req,'events/show_event.html', {})
#
def add_event(req):
    return render(req,'events/add_event.html', {})

def bylaw(req):
    return render(req,'bylaw.html', {})

def contact(req):
    if req.method == 'GET':
        return render(req,'contact.html', {})
    else:
        form = ContactForm(req.POST,req.FILES)
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

def generate_qr_code(req):

    img_bg = Image.open('static/website/img/core-img/cross.jpg')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('https://ethio-church-website.herokuapp.com/')

    img = qr.make(fit=True)
    img_qr = qr.make_image()
    pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])
    img_bg.paste(img_qr, pos)
    img_bg.save('churchwebsite.png')
    return FileResponse(open('churchwebsite.png', 'rb'),as_attachment=True,filename='churchwebsiteQRCode.png')