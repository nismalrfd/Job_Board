from django import forms

from jobs.models import JobListing, Employer, Application


class NewJobForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ('category', 'title', 'location', 'description', 'expired')


class EditJobForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ('category', 'title', 'location', 'description', 'expired')


class EmployerUserForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('company_name', 'contact_email', 'website', 'description', 'logo')

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'resume', 'cover_letter']
