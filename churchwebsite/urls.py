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
    path('admin_page', views.admin_page, name='admin_page'),
    path('doctrinal', views.doctrinal, name='doctrinal'),
    path('spritual',views.spritual,name='spritual'),
    path('bible',views.bibleStudy,name='bible'),
    path('all_events',views.all_events,name='all_events'),
    path('update_event/<event_id>',views.update_event,name='update_event'),
    path('delete_event/<event_id>', views.delete_event, name='delete_event'),
    path('generate_qr_code',views.generate_qr_code,name='qrcode'),
    #
    path('event_approval',views.admin_event_approval,name='event_approval'),
]
