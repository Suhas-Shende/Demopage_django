from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
def  home(request):
    return HttpResponse("hello")
    return render(request,'index.html',{})