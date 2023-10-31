from django.shortcuts import render
from django.http import HttpResponse
from.models import data

def home(request):
    if request.method=='post':
        mail=request.post['email']
        contact=request.post['contact']
        obj=data()
        obj.email
        obj.contact
        obj.save()
    return render(request,'index.html')


