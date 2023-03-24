from django.shortcuts import render, redirect
from datetime import date
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpRequest, HttpResponse
from .smtplib import ContactForm
import qrcode
from PIL import ImageDraw
from PIL import ImageFont
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
    print(f'req {req}')
    #print(f'option {data}')
    #,data ='https://ethio-church-website.herokuapp.com/'
    """qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )"""
    qr = qrcode.QRCode(box_size=20)
    qr.add_data('https://ethio-church-website.herokuapp.com/')

    # qr.make(fit=True)
    img = qr.make_image()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('bahnschrift.ttf',30)
    draw.text((80,750),'Debre Bisrat Saint Gabriel & Arsema website link',font=font)
    #draw.text((300,550),name,font=font)
    # img = qr.make_image(fill_color="black", back_color="white")
    # img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
    # Save the imgae as an image file
    #img.save('churchwebsite.jpg')
    img.show('churchwebsite.jpg')
    return redirect("index")