from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from employer.forms import NewJobForm, EditJobForm, EmployerUserForm
from jobs.models import *


# Create your views here.
def employerRegister(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.warning(request, 'username already exists')
                return redirect('employer:employerRegister')
            if confirm_password and password and password != confirm_password:
                messages.warning(request, 'password not matching !')
                return redirect('employer:employerRegister')

            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()

            # Profile.objects.create(user= user_obj,token = genarate_random_string(20))

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



def update_employer_profile(request):
    user=request.user

    form = EmployerUserForm(instance=user)

    if request.method == 'POST':
        form = EmployerUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('employer:employer')

    context = {
        'form': form,
        'user':user
    }

    return render(request, 'employer/employer_profile.html',context)
