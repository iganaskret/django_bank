from bank_app.models import Customer
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import django_rq
from . messaging import email_message


def login(request):
    context = {}

    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user:
            dj_login(request, user)
            return HttpResponseRedirect(reverse('bank_app:index'))
        else:
            context = {
                'error': 'Bad username or password.'
            }
    return render(request, 'login_app/login.html', context)


@login_required
def logout(request):
    dj_logout(request)
    return render(request, 'login_app/login.html')


def sign_up(request):
    context = {}
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        rank = request.POST['rank']
        username = request.POST['username']
        user = User.objects.create_user(
            email=email, username=username, password=password, first_name=first_name, last_name=last_name)
        # new_user= User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        # new_user.save()
        if password == confirm_password:
            if Customer.objects.create(user=user, phone_number=phone, rank=rank):
                django_rq.enqueue(email_message, {
                    'email': email,
                    'username': username,
                    'password': password,
                })
                return HttpResponseRedirect(reverse('login_app:login'))

            else:
                context = {
                    'error': 'Could not create user account - please try again.'
                }
        else:
            context = {
                'error': 'Passwords did not match. Please try again.'
            }

    return render(request, 'login_app/sign_up.html', context)
