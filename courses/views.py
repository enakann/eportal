from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def my_first_view(request):
    return render(request,'courses/hello.html',{'who':"fuck face" })
