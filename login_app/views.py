from bank_app.models import Customer
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from . models import ActivateAccount

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
        #new_user= User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        # new_user.save()
        if password == confirm_password:
            if Customer.objects.create(user=user, phone_number=phone, rank=rank):
                return HttpResponseRedirect(reverse('login_app:activate_account'))
            else:
                context = {
                    'error': 'Could not create user account - please try again.'
                }
        else:
            context = {
                'error': 'Passwords did not match. Please try again.'
            }
    return render(request, 'login_app/sign_up.html', context)


def request_activate_account(request):
    if request.method == "POST":
        post_user = request.POST['username']
        user = None

        if post_user:
            try:
                user = User.objects.get(username=post_user)
            except:
                print(f"Invalid Activate Account Token Request: {post_user}")
        else:
            post_user = request.POST['email']
            try:
                user = User.objects.get(email=post_user)
            except:
                print(f"Invalid Activate Account Token Request: {post_user}")
        if user:
            prr = ActivateAccountTokenRequest()
            prr.user = user
            prr.save()
            django_rq.enqueue(email_message, {
                'token': prr.token,
                'email': prr.user.email,
            })
            return HttpResponseRedirect(reverse('login_app:activate_account'))

    return render(request, 'login_app/activate_account.html')


def activate_account(request):
    if request.method == "POST":
        #   post_user = request.POST['username']
        #   password = request.POST['password']
        #   confirm_password = request.POST['confirm_password']
        #   token = request.POST['token']

        #   if password == confirm_password:
        #       try:
        #           prr = PasswordResetRequest.objects.get(token=token)
        #           prr.save()
        #       except:
        #           print("Invalid password reset attempt.")
        #           return render(request, 'login_app/password_reset.html')

        #       user = prr.user
        #       user.set_password(password)
        #       user.save()
        return HttpResponseRedirect(reverse('login_app:login'))

    return render(request, 'login_app/activate_account.html')
