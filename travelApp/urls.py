from django.urls import path
from .import views



urlpatterns = [
    path('',views.user_login,name='user_login'),
    path('home',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('booking/',views.booking,name='booking'),
    path('user_login/',views.user_login,name='user_login'),
    path('success_contact/',views.success_contact,name='success_contact'),
    path('user_register/',views.user_register,name='user_register'),
    

]
