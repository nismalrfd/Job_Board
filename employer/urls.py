from django.urls import path
from . import views

app_name = 'employer'


urlpatterns = [
    path('adminregister',views.adminregister,name='adminregister'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('adminpage', views.adminpage, name='adminpage'),

]
