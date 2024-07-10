from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "plano/home.html")

def about(request):
    return render(request, "plano/about.html")

def contacto(request):
    return render(request, "plano/contacto.html")