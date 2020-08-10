from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.

def formular(request):
    return render(request, 'form_template.html')



