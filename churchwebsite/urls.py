from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),   
    path('about', views.about, name='about'),
    path('bylaw', views.bylaw, name='bylaw'),   
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),   
    path('events', views.events, name='events'),
    path('doctrinal', views.doctrinal, name='doctrinal'),
    path('spritual',views.spritual,name='spritual'),
    path('bible',views.bibleStudy,name='bible')
]
