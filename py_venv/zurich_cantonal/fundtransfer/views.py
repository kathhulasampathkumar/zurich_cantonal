from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.core import serializers
from django.core.files.storage import FileSystemStorage

from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt 
from user_master.models import user_master

# Create your views here.
def index (request):
    if 'user_id' in request.session:
        del request.session['user_id']  # or request.session.pop('user_id', None)    
        context={'title':'Home'}
        return render(request,'index_form.html',context)
    else :
        # del request.session['user_id']  # or request.session.pop('user_id', None)    
        context={'title':'Home'}
        return render(request,'index_form.html',context)
def home(request):    
    user_id=request.session.get('user_id')
    context={'title':'HomePage','user_id':user_id}
    return render(request,'index.html',context)
def getUserData(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email)
        # print(password)        
        if user_master.objects.filter(email=email,password=password,status=1).exists():
            user = user_master.objects.filter(email=email,password=password,status=1).get()
            if user.id is not None :
                request.session['user_id']=user.id   
                user_id = request.session.get('user_id') 
                context={'title':'HomePage','user_id':user_id}
                return render(request,'dashboard.html',context)
            else :
                messages.add_message(request,messages.WARNING,'Invalid Credentials. Please enter valid credentials.')
                return redirect('index')
        else :
            messages.add_message(request,messages.WARNING,'Invalid Credentials. Please enter valid credentials.')
            return redirect('index')
    else :
        return redirect('index')




    # return HttpResponse('you are requested homepage')
