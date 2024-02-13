from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return HttpResponse("Hello, World! \n From Django!")

def goodbye(request):
    return HttpResponse("Goodbye, World! \n From Django!")
