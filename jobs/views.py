from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from employer.forms import JobApplicationForm
from jobs.models import *


# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            full_name = request.POST.get('full_name')
            contact_email = request.POST.get('contact_email')
            skills = request.POST.get('skills')
            resume = request.POST.get('resume')
            profile_picture = request.POST.get('profile_picture')

            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.warning(request, 'Username already exists')
                return redirect('registerPage')

            if confirm_password != password:
                messages.warning(request, 'Passwords do not match')
                return redirect('registerPage')

            user = User(username=username)
            user.set_password(password)
            user.save()

            jobseeker = JobSeeker(
                user=user,
                full_name=full_name,
                contact_email=contact_email,
                skills=skills,
                resume=resume,
                profile_picture=profile_picture,
            )
            jobseeker.save()

            login(request, user)

            messages.success(request, 'Account created')
            return redirect('login')
        except Exception as e:
            messages.warning(request, 'Something went wrong')

    return render(request, 'signup.html')


def loginPage(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            from django.contrib.auth.models import User
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.warning(request, 'User not Found ')
                return redirect('/loginPage')
            # if not Profile.objects.filter(user = user_obj).first().is_verified:
            #     messages.warning(request, 'your profile not verified..')
            #     raise Exception('profile not verified')
            #
            user_obj = authenticate(username=username, password=password)

            if user_obj:
                login(request, user_obj)
                return redirect('/user')

            messages.warning(request, 'wrong password ')
            return redirect('loginPage')

        except Exception as e:
            messages.warning(request, 'Something went wrong')

    return render(request, 'login.html')


def user(request):
    job = JobListing.objects.all()

    applications = Application.objects.filter(applicant__user=request.user)
    context = {
        'jobs': job,
        'applications': applications

    }
    return render(request, 'user.html', context)


# def apply_for_job(request, pk):
#     job = JobListing.objects.get(pk=pk)
#     user = request.user
#
#
#     # if Application.objects.filter(job=job,applicant=user).exists():
#     #     messages.warning(request,'already applied')
#     #     return redirect('user')
#
#     if request.method == 'POST':
#         form = JobApplicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             application = form.save(commit=False)
#             application.job = job
#             application.applicant = user
#
#             application.save()
#             return redirect('user')
#     else:
#         form = JobApplicationForm()
#
#     return render(request, 'job_application.html', {'form': form, 'job': job})
#
#
#
def apply_for_job(request, pk):

    job = JobListing.objects.get(pk=pk)

    applicant, created = JobSeeker.objects.get_or_create(user=request.user)

    if Application.objects.filter(job=job, applicant=applicant).exists():
        messages.warning(request, 'already applied')
        return redirect('user')

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = applicant
            application.save()

            employer_email = job.created_by.email  # Assuming the employer's email is stored in the User model
            subject = f'New Job Application for {job.title}'
            message = f'A user has applied for the job: {job.title}. Please find the applicant\'s resume attached.'
            from_email = 'your-email@example.com'  # The sender's email address
            recipient_list = [employer_email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return redirect('user')

    else:
        form = JobApplicationForm()

    return render(request, 'job_application.html', {'form': form})
