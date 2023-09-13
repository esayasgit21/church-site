# Super user event form
from django import forms
from django.forms import ModelForm
from .models import Course, Event, ImageData2

# Admin SuperUser Event Form
class AdminEventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'location', 'manager', 'attendees', 'description')
		labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD HH:MM',
			'location': '',
			'manager': 'Manager',
			'attendees': '',
			'description': '',			
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			'location': forms.TextInput(attrs={'class':'form-select', 'placeholder':'Location'}),
			'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
			'attendees': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Attendees'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
		}

class ImageForm(ModelForm):
	class Meta:
		model = ImageData2
		fields = ('title', 'body', 'image','web_link','path')
		labels = {
			"title":'',
			"body" : '',
			"image" : '',
			'web_link': '',
			'path':'',
		}
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image Title'}),
			'body': forms.Textarea(attrs={'rows':4, 'cols':15, 'class':'form-control', 'placeholder':'Description'}),
			'web_link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Address'}),
			'path': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image Path'}),
		}

# Course regestration

GRADE_CHOICES= [
    ('one', 'First Grade'),
    ('two', 'Second Grade'),
    ('three', 'Third Grade'),
    ('decon', 'Decon'),
    ]

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ('subject', 'web_link', 'grade','description','image')
		labels = {
			"subject":'',
			'web_link': '',
			'grade' : '',
			"description" : '',
			"image" : '',
			
		}
		widgets = {
			'subject': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}),
			'web_link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Address'}),
			'grade': forms.Select(choices = GRADE_CHOICES, attrs={'class':'form-select', 'placeholder':'Student Grade'}),
			'description': forms.Textarea(attrs={'rows':4, 'class':'form-control', 'placeholder':'Description'}),
		}	

# User Event Form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'location', 'attendees', 'description')
		labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD HH:MM',
			'location': '',
			#'manager': 'Manager',
			'attendees': '',
			'description': '',			
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event location'}),
			#'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
			'attendees': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Attendees'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
		}


