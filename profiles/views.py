from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def details(request):
    return HttpResponse("This is details")


def delete(request):
    return HttpResponse("This is delete")