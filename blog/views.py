from django.shortcuts import render
from django.http import HttpResponse

# Create your views here:
def showblog(request):
    return HttpResponse("you are seeing the blog entries now !")