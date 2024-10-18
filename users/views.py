from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

from users.forms import CustomUserCreationForm


class UserRegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'users/signup.html', {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

        return render(request, 'users/signup.html', {"form": form})


class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, 'users/login.html', {"form": form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You have successfully logged out')
        return redirect('home')

