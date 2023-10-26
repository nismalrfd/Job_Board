# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
#
#
# # Create your views here.
# def registerPage(request):
#     if request.method == 'POST':
#         try:
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             confirm_password = request.POST.get('confirm_password')
#
#             user_obj = User.objects.filter(username=username)
#             if user_obj.exists():
#                 messages.warning(request, 'username already exists')
#                 return redirect('/register')
#             if confirm_password and password and password != confirm_password:
#                 messages.warning(request, 'password not matching !')
#                 return redirect('/register')
#
#             user_obj = User.objects.create(username=username)
#             user_obj.set_password(password)
#             user_obj.save()
#
#             # Profile.objects.create(user= user_obj,token = genarate_random_string(20))
#
#             messages.success(request, 'Account created')
#             return redirect('login')
#         except Exception as e:
#             messages.warning(request, 'Something went wrong')
#
#     return render(request,'signup.html')
# def loginPage(request):
#     if request.method == 'POST':
#         try:
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#
#             from django.contrib.auth.models import User
#             user_obj = User.objects.filter(username=username)
#             if not user_obj.exists():
#                 messages.warning(request, 'User not Found ')
#                 return redirect('/login')
#             # if not Profile.objects.filter(user = user_obj).first().is_verified:
#             #     messages.warning(request, 'your profile not verified..')
#             #     raise Exception('profile not verified')
#             #
#             user_obj = authenticate(username=username, password=password)
#
#             if user_obj:
#                 login(request, user_obj)
#                 return redirect('/user')
#
#             messages.warning(request, 'wrong password ')
#             return redirect('login')
#
#         except Exception as e:
#             messages.warning(request, 'Something went wrong')
#
#     return render(request, 'login.html')
#
#
# def user(request):
#     return render(request,'user.html')