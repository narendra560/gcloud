from turtle import reset
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

from app1 import models
def homepage(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        response="<h1><a href=\"http://127.0.0.1:8000/create\">Create Mcq</a> </h1><h1><a href=\"http://127.0.0.1:8000/viewmcqs\">View Mcqs</a></h1>" 

        return HttpResponse(response)
def create(request):
    return render(request,"mcqs.html")
def save(request):
    if(request.method=="POST"):
        d={}
        for i in request.POST:
            if("csrf" not in i):
                d[i]=request.POST[i]
        ans=models.createMCQ(d)
        response="<h1>Creation Successful</h1>"
    return HttpResponse(response)
def viewMCQ(request):
    mcqs=models.fetchMCQS()
    print(list(mcqs))
    return render(request,"viewmcqs.html",{'mcqs':mcqs})
    