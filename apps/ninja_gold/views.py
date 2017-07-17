from django.shortcuts import render, redirect

def index(request):
    return render(request, 'ninja_gold/index.html')