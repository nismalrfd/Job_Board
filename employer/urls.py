from django.urls import path


from . import views

app_name = 'employer'


urlpatterns = [
    path('employerLogin/',views.employerLogin,name='employerLogin'),
    path('employerRegister/', views.employerRegister, name='employerRegister'),
    path('employer/', views.employer, name='employer'),
    path('userDetails/<int:pk>', views.userDetails, name='userDetails'),

    path('create_job_listing/', views.create_job_listing, name='create_job_listing'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.edit, name='edit'),

    path('update_employer_profile/', views.update_employer_profile, name='update_employer_profile'),
    path('logout', views.logout_view, name='logout'),

    path('validate-username/', views.validate_username, name='validate_username'),

    ]
