from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        User.objects.create_user(username = username, password = password, phone = phone, address = address)
        return redirect ('user:login')


def login(request):
    return render(request, 'login.html')        



