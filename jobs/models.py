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
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    expired = models.BooleanField(default=False)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
