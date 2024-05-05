from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
from .forms import CreateNewUser, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/signup.html', context={'title': 'Sign up', 'form': form})


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Content:home'))

    return render(request, 'App_Login/login.html', context={'title': 'Login', 'form': form})


@login_required
def profile(request):
    return render(request, 'App_Login/profile.html')


@login_required
def edit_profile(request):
    user_profile = request.user.user_profile

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('App_Login:profile'))
    else:
        form = EditProfileForm(instance=user_profile)

    return render(request, 'App_Login/edit_profile.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))
