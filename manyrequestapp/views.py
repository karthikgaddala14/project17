from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
class GetInput(View):
    def get(self,request):
        return render(request,'getinput.html')
class PostInput(View):
    def get(self,request):
        return render(request,'postinput.html')
class Add(View):
    def get(self,request):
        i=int(request.GET["t1"])
        j=int(request.GET["t2"])
        k=i+j
        return HttpResponse("The sum is: "+str(k))
    def post(self,request):
        x=int(request.POST["t1"])
        y=int(request.POST["t2"])
        z=x+y
        return HttpResponse("The sum is: "+str(z))
