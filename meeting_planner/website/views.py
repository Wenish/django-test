from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")

def now(request):
    today = date.today()
    response = "Today's date: ", today.strftime("%d.%m.%y")
    return HttpResponse(response)