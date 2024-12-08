from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# /music/goods
def goods(request):
    return HttpResponse("music的goods")
