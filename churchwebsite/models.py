from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Service(models.Model):
    image = models.ImageField(upload_to='website/', blank=True, null=True)
    title = models.CharField(max_length=155)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class ImageData(models.Model):
    title = models.CharField(max_length=120, blank = False)
    body = models.TextField(max_length=255,blank = True)
    web_link = models.URLField('Website Address', blank = True)
    image = models.ImageField(upload_to='img/', blank = False, null = True)

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField('Location Name',max_length=120)
    address = models.CharField(max_length=240)
    zip_code = models.CharField('Zip Code', max_length=5)
    phone = models.CharField('Contact Phone',max_length=15, blank=True)
    location_image = models.ImageField(null=True, blank=True, upload_to="website/img/events")
    organizer = models.IntegerField("Organizer",blank=False, default=1)

    def __str__(self):
        return self.name
    
class churchUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ',' + self.last_name
    
class Course(models.Model):
    subject = models.CharField('Course Name',max_length=120)
    web_link = models.URLField('Website Address', blank = True)
    grade = models.CharField('Grade',max_length=40)
    description = models.TextField(blank = True)
    image = models.FileField(upload_to='course/', blank = True, null = True)
    #manager = models.ForeignKey(User, blank=True,null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.subject

class Event(models.Model):
    name = models.CharField('Event Name',max_length=120)
    event_date = models.DateTimeField('Event Date')
    #location = models.ForeignKey(Location, blank=True, null=True, on_delete= models.CASCADE)
    location = models.CharField('Event Location',max_length=200)
    attendees = models.CharField('Participants',max_length=120)
    manager = models.ForeignKey(User, blank=True,null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank = True)
    approved = models.BooleanField('Approved', default=False)

    def __str__(self):
        return self.name
    
    @property
    def Delete_Expried_Event(self):
        today = date.today()
        days_till = self.event_date.date() - today
        days_till_stripped = str(days_till).split(",", 1)[0]
        print(f'days_till{days_till_stripped.split(" ",1)[0]}')
        if int(days_till_stripped.split(" ",1)[0]) < -7:
            return 20
        else:
            return days_till_stripped
    
    @property
    def Days_Till(self):
        today = date.today()
        days_till = self.event_date.date() - today
        days_till_stripped = str(days_till).split(",", 1)[0]
        return days_till_stripped
    
    @property
    def Is_Past(self):
        today = date.today()
        if self.event_date.date() < today:
            thing = 'Past'
        else:
            thing = 'In The Future'
        return thing
