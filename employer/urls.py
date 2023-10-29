from django.conf.urls.static import static
from django.urls import path

from Jobnest import settings
from . import views

app_name = 'employer'


urlpatterns = [
    path('employerLogin/',views.employerLogin,name='employerLogin'),
    path('employerRegister/', views.employerRegister, name='employerRegister'),
    path('employer/', views.employer, name='employer'),


    path('create_job_listing/', views.create_job_listing, name='create_job_listing'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.edit, name='edit'),

    path('update_employer_profile/', views.update_employer_profile, name='update_employer_profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)