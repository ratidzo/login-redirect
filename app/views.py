from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def login(request):
    # Handle your login here and redirect on success.
    return redirect('congrat')


def congrat(request):
    return render(request, "login/congratulation.html")
