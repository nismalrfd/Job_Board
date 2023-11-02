from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



from jobs import views

urlpatterns = [
    path('', views.user, name='user'),

    path('registerPage',views.registerPage,name='registerPage'),
    path('login', views.loginPage, name='login'),
    path('job_details/<int:pk>', views.job_details, name='job_details'),

    path('user_profile_update/', views.user_profile_update, name='user_profile_update'),

    path('apply_for_job/<int:pk>', views.apply_for_job, name='apply_for_job'),
    path('update_profile', views.update_profile, name='update_profile'),

    path('logout', views.logout_view, name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
