from django.contrib import admin
from django.urls import path, include

from jobs import views

urlpatterns = [
    path('registerPage',views.registerPage,name='registerPage'),
    path('login', views.loginPage, name='login'),
    path('user', views.user, name='user'),

    path('apply_for_job/<int:pk>', views.apply_for_job, name='apply_for_job'),

]
