from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	return render(request, "Home.html", {})

def discover_view(request, *args, **kwargs):
	return render(request, "discover.html", {})