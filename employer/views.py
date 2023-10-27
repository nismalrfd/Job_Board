from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from employer.forms import NewJobForm, EditJobForm, EmployerUserForm
from jobs.models import *

def employerRegister(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            company_name = request.POST.get('company_name')
            contact_email = request.POST.get('contact_email')
            website = request.POST.get('website')
            description = request.POST.get('description')
            logo = request.FILES.get('logo')

            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.warning(request, 'Username already exists')
                return redirect('employer:employerRegister')

            if confirm_password != password:
                messages.warning(request, 'Passwords do not match')
                return redirect('employer:employerRegister')

            user = User(username=username)
            user.set_password(password)
            user.save()

            employer = Employer(
                user=user,
                company_name=company_name,
                contact_email=contact_email,
                website=website,
                description=description,
                logo=logo,
            )
            employer.save()

            login(request, user)

            messages.success(request, 'Account created')
            return redirect('employer:employerLogin')
        except Exception as e:
            messages.warning(request, 'Something went wrong')

    return render(request, 'employer/signup.html')



def employerLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)
        if not user_obj.exists():
            messages.warning(request, 'User not Found ')
            return redirect('/employerLogin')
        # if not Profile.objects.filter(user = user_obj).first().is_verified:
        #     messages.warning(request, 'your profile not verified..')
        #     raise Exception('profile not verified')
        #
        user_obj = authenticate(username=username, password=password)

        if user_obj:
            login(request,user_obj)
            return redirect('employer:employer')

        messages.warning(request, 'wrong password ')
        return redirect('employer:employerLogin')

    return render(request, 'employer/login.html')


def employer(request):
    jobs= JobListing.objects.filter(created_by=request.user)
    context={
        'jobs':jobs
    }
    return render(request, 'employer/adminpage.html',context)


def create_job_listing(request):
    if request.method == 'POST':
        form = NewJobForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('employer:employer')
    form = NewJobForm()
    context = {
        'form': form
    }

    return render(request, 'employer/create_job_listing.html', context)


def delete(request, pk):
    jobs = JobListing.objects.get(pk=pk,created_by=request.user)
    jobs.delete()
    return redirect('employer:employer')


def edit(request, pk):
    jobs = JobListing.objects.get(pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditJobForm(request.POST, instance=jobs)
        if form.is_valid():
            form.save()
            return redirect('employer:employer')

    form = EditJobForm(instance=jobs)
    context = {
        'form': form
    }
    return render(request, 'employer/edit_job_listing.html', context)




# def update_employer_profile(request):
#     jobs = Employer.objects.get(user=request.user)
#
#     if request.method == 'POST':
#         form = EmployerUserForm(request.POST, request.FILES, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return redirect('employer:employer')  # Redirect to the employer's dashboard or profile page
#     else:
#         form = EmployerUserForm(instance=jobs)
#     context = {
#         'form': form,
#         'jobs':jobs
#     }
#
#     return render(request, 'employer/employer_profile.html', context)


def update_employer_profile(request):
    employer = Employer.objects.get(user=request.user)

    if request.method == 'POST':
        form = EmployerUserForm(request.POST, request.FILES, instance=employer)

        if form.is_valid():
            form.save()
            return redirect('employer:employer')
    else:
        form = EmployerUserForm(instance=employer)

    context = {
        'form': form,
        'employer': employer
    }

    return render(request, 'employer/employer_profile.html', context)