from django.shortcuts import redirect, render

# Create your views here.
def  home(request):
    return HttpResponse("hello")
    return render(request,'index.html',{})