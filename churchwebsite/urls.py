from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),   
    path('about', views.about, name='about'),
    path('bylaw', views.bylaw, name='bylaw'),   
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),   
    path('show_event', views.events, name='show_event'),
    path('add_course', views.add_course, name='add_course'),
    path('add_event', views.add_event, name='add_event'),
    path('admin_page', views.admin_page, name='admin_page'),
    path('doctrinal', views.doctrinal, name='doctrinal'),
     path('eotc', views.etoc, name='eotc'),
    path('spritual',views.spritual,name='spritual'),
    path('bible',views.bibleStudy,name='bible'),
    path('all_events',views.all_events,name='all_events'),
    path('all_course',views.all_course,name='all_course'),
    path('update_event/<event_id>',views.update_event,name='update_event'),
    path('delete_event/<event_id>', views.delete_event, name='delete_event'),
    path('update_course/<course_id>',views.update_course,name='update_course'),
    path('delete_course/<course_id>', views.delete_course, name='delete_course'),
    path('generate_qr_code',views.generate_qr_code,name='qrcode'),
    path('delete_image/<image_id>', views.delete_image, name='delete_image'),
    path('event_approval',views.admin_event_approval,name='event_approval'),
    path('download_file/<int:course_id>/', views.download_file, name = 'download_file')
]
