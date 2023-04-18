import json
from django.conf import settings
from .models import Course, Event, ImageData
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from django.core.mail import send_mail
from django.http import BadHeaderError, FileResponse, Http404, HttpResponse
from django.contrib import messages
from churchwebsite.forms import AdminEventForm, CourseForm, EventForm, ImageForm
from .smtplib import ContactForm
import qrcode
from os import path
import mimetypes
import os
import codecs
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image
from django.http import HttpResponseRedirect
# Import User Model From Django
from django.contrib.auth.models import User
# Create your views here.

from django.core.management.utils import get_random_secret_key



def index(req):
    todayYear = date.today().year
    #print(f'get {get_random_secret_key()}')
    #filePath = 'static/website/json/img_path.json'
    #with codecs.open(filePath,'r',encoding='utf-8', errors='strict') as image_file:  
        #data = json.load(image_file)
    image_list = ImageData.objects.all().order_by('-id')
    return render(req,'index.html', {
        'year':todayYear,
        'image_list':image_list
        })

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

def admin_page(req):
    submitted = False
    image_list = ImageData.objects.all().order_by('-id')
    count = len(image_list) 
    if req.method == 'POST':
        form = ImageForm(req.POST, req.FILES)
        file = req.FILES['image']
        if len(req.FILES) != 0 and file.size < 1048576:
            if form.is_valid:
                form.save()
            # save file into json and upload image
                return HttpResponseRedirect('admin_page?submitted=True')
        else:
            if bool(req.FILES.get('image', False)) == True:
                msg = 'Error: File too large. Size should not exceed 1 MiB.'
            return render(req,'admin_page.html',{
                'msg': msg,
                'form': ImageForm,
            })
    else:
        form = ImageForm
        if 'submitted' in req.GET:
            submitted = True

    return render(req,'admin_page.html', {
                'image_list': image_list,
                'form': form,
                'submitted' : submitted,
                'count' : count,
                'msg': False,
                })

def select_data(data, path, filename):
    i= 0
    for i in range(len(data)):
        ele_path = data[i]['img_path']
        ele_name = data[i]['name']
        if path == ele_path and ele_name == filename:
            return i
    i = i + 1

def loda_jsonData():
    # Check if file exists
    filePath = 'static/website/json/img_path.json'
    if path.isfile(filePath) is False:
        raise Exception("File not found")

    with codecs.open(filePath,'r',encoding='utf-8', errors='strict') as image_file:  
        data = json.load(image_file)
    return data 

def write_json(new_data):
    with open('static/website/json/img_path.json','r+',encoding='utf-8', errors='strict') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def delete_image(req,image_id):

    imageData = ImageData.objects.get(pk=image_id)
    if req.user.is_superuser:
        imageData.delete()
        messages.success(req, ("Selected Image Deleted Successfully!!"))
        return redirect('admin_page')
    else:
        messages.success(req, 'You are not Authorized To Remove selected Image')
        return redirect('login')

def all_events(req):
    event_list = Event.objects.all().order_by('event_date')
    event_count = len(event_list.filter(approved = True))
    return render(req,'events/all_events.html', {
        'event_list': event_list,
        'event_count' : event_count
    })

def all_course(req):
    course_list = Course.objects.all().order_by('subject')
    return render(req,'course/all_course.html',
        {
            'course_list': course_list
        })

def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	"""if request.user.is_superuser:
		form = EventFormAdmin(request.POST or None, instance=event)	
	else:
		form = EventForm(request.POST or None, instance=event)"""
	form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('all_events')

	return render(request, 'events/update_event.html', 
		{
            'event': event,
            'form':form
        })

def update_course(req, course_id):
    course = Course.objects.get(pk=course_id)
    form = CourseForm(req.POST or None, instance=course)

    if form.is_valid():
        form.save()
        return redirect('all_course')

    return render(req, 'course/update_course.html', 
		{
            'course': course,
            'form':form
        })

def delete_course(req,course_id):
    course = Course.objects.get(pk=course_id)
    if req.user != "course.manager":
        course.delete()
        messages.success(req, ("Course Deleted Successfully!!"))
        return redirect('all_course')
    else:
        messages.success(req, 'You are not Authorized To Delete selected Course')
        return redirect('all_course')

def delete_event(req,event_id):
    event = Event.objects.get(pk=event_id)
    if req.user == event.manager:
        event.delete()
        messages.success(req, ("Event Deleted Successfully!!"))
        return redirect('all_events')
    else:
        messages.success(req, 'You are not Authorized To Delete selected Event')
        return redirect('all_events')
    
def add_course(req):
    submitted = False
    if req.method == 'POST':
        form = CourseForm(req.POST, req.FILES)
        print(f'form {req.user}')
        if form.is_valid():
            course = form.save()
            course.manager = req.user
            course.save()
            #form.save()
        return HttpResponseRedirect('/add_course?submitted=True')
    else:
        form = CourseForm()    
        if 'submitted' in req.GET:
            submitted = True
    return render(req, 'course/add_course.html', 
        {
        'form':form, 
        'submitted': submitted
        })

def add_event(req):
    submitted = False

    if req.method == 'POST':
        if req.user.is_superuser:
            form = AdminEventForm(req.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_event?submitted=True')
        else:
            form = EventForm(req.POST)
            if form.is_valid():
                #form.save()
                event = form.save(commit=False)
                event.manager = req.user
                event.save()
                return HttpResponseRedirect('/add_event?submitted=True')    
    else:
        # Not Submitted
        if req.user.is_superuser:
            form = AdminEventForm()
        else:
            form = EventForm()    
        if 'submitted' in req.GET:
            submitted = True
    return render(req, 'events/add_event.html', {'form':form, 'submitted': submitted})

"""def add_image(req):

    submitted = False
    if req.method == 'POST':
        form = ImageData(req.POST, req.FILES)
        print(f'form {req.user}')
        if form.is_valid():
            course = form.save()
            course.manager = req.user
            course.save()
            #form.save()
            return HttpResponseRedirect('admin_page?submitted=True')
        else:
            return 
    else:
        form = ImageData()    
        if 'submitted' in req.GET:
            submitted = True
    return render(req, 'admin_page.html', 
        {
        'form':form, 
        'submitted': submitted
        })"""

# Create Admin Event Approval Page
def admin_event_approval(req):
	# Get Counts
    event_count = Event.objects.all().count()
    user_count = User.objects.all().count()
        
    event_list = Event.objects.all().order_by('-event_date')

    if req.user.is_superuser:

        if req.method == 'POST':
            # set up list of checked box id's
            id_list = req.POST.getlist('boxes')

            # unckecked 
            event_list.update(approved = False)

            # update backend database

            for id in id_list:
                event_list.filter(pk = int(id)).update(approved = True)
            # Show Success Message and Redirect
            messages.success(req,('Approvel has been updated successfully!'))
            return redirect('all_events')
        else:
            return render(req,'events/event_approval.html',{
                'event_list': event_list,
                'event_count': event_count,
                'user_count': user_count
            })
    else:
        messages.success(req,("You are not authorized to view this page!"))
        return redirect('index')
    
    #return render(req,'events/event_approval.html')

def generate_qr_code(req):
    file_path = 'static/website/img/core-img/qrcodeimg.jpg'
    generatewd_file_path = 'static/website/img/core-img/churchwebsiteQrcode.png'
    file_exists = path.exists(generatewd_file_path)
    if file_exists is True:
        return FileResponse(open(generatewd_file_path, 'rb'),as_attachment=True,filename=generatewd_file_path) 
    else:
        img_bg = Image.open(file_path) 
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('https://ethio-church-website.herokuapp.com/')

        #img = qr.make(fit=True)
        img_qr = qr.make_image()
        pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])
        img_bg.paste(img_qr, pos)
        file_name = generatewd_file_path
        img_bg.save(file_name)
        return FileResponse(open(file_name, 'rb'),as_attachment=True,filename=file_name)
    

# download course

def download_file(req, course_id):
    # fill these variables with real values
    file = get_object_or_404(Course,pk=course_id)
    path = '/media/course'
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    print(f'file_path{file_path}')
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(file.image, content_type=mime_type)
    response['Content-Disposition'] = f'attachment; filename="{file.image.name}"'
    return response