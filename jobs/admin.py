from django.contrib import admin

from jobs.models import *

# Register your models here.
admin.site.register(Employer)
admin.site.register(Category)
admin.site.register(JobListing)
admin.site.register(JobSeeker)
admin.site.register(Application)