from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellow world, this is the index")

