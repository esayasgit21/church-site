# Super user event form
from django import forms
from django.forms import ModelForm
from .models import Event, ImageData

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
		model = ImageData
		fields = ('title', 'body', 'image','web_link')
		labels = {
			"title":'',
			"body" : '',
			"image" : '',
			'web_link': '',
		}
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image Title'}),
			'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
			'web_link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Address'}),
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


