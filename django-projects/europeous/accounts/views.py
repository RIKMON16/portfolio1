from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def acc(request):
    return HttpResponse('This is accounts app')
