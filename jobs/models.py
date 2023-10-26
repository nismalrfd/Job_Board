from django.contrib.auth.models import User
from django.db import models


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # If using the built-in User model
    company_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='employer_logos/', blank=True, null=True)

    def __str__(self):
        return self.company_name


class Category(models.Model):
    name = models.CharField(max_length=255)

    # for correct in admin panel
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class JobListing(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    expired = models.BooleanField(default=False)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # If using the built-in User model
    full_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    skills = models.TextField()
    resume = models.FileField(upload_to='job_seeker_resumes/', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='job_seeker_profile_pics/', blank=True, null=True)


class Application(models.Model):
    job_employer = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    # Add more fields specific to applications
