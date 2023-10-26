from django import forms

from jobs.models import JobListing, Employer


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
