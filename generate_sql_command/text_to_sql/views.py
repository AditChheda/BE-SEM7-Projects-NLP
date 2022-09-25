from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
        return render(request, 'text_to_sql/home.html')