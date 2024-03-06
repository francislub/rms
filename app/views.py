from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def login(request):
    return render(request, 'dashboard.html')
