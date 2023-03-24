from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),   
    path('about', views.about, name='about'),
    path('bylaw', views.bylaw, name='bylaw'),   
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),   
    path('show_event', views.events, name='show_event'),
    path('add_event', views.add_event, name='add_event'),
    path('doctrinal', views.doctrinal, name='doctrinal'),
    path('spritual',views.spritual,name='spritual'),
    path('bible',views.bibleStudy,name='bible'),
    path('^generate_qr_code',views.generate_qr_code,name='script'),
    #path('qrcode/<int:id>/',views.generate_qr_code,name='qrcode'),
    #path('^qrcode/<data>/',views.generate_qr_code,name='qrcode'),
]
