from django import forms

from jobs.models import JobListing, Employer, Application, JobSeeker

INPUT_CLASSES = 'w-full border rounded-md p-2'

class NewJobForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ('category', 'title', 'location', 'description', 'expired')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'location': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),

        }


class EditJobForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ('category', 'title', 'location', 'description', 'expired')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'location': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'expired': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class EmployerUserForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('company_name', 'contact_email', 'website', 'description', 'logo')
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'contact_email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),
            'website': forms.URLInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'logo': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditUserForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ('full_name', 'contact_email', 'resume', 'skills', 'profile_picture')
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'contact_email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),

            'skills': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'resume': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


INPUT_CLASSES1 = 'w-full p-3 border border-gray-400 rounded-lg focus:outline-none focus:border-blue-500'

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'resume', 'cover_letter']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES1
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),
            'resume': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'cover_letter': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),

        }
