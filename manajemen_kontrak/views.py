from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'main.html')

