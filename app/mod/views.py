from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def db_vacuum(request):

    a = []
    for i in range(0,100):
        print i

    return HttpResponse()