from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import *
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from models import *
# Create your views here.

class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    birthdate = forms.DateField()
    gender = forms.CharField(max_length=2)
    position = forms.CharField(max_length=25)

def index(request):
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)
   
    return render(request, 'form1/index.html')
    
    
  
def addperson(request):
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = request.user
            ps = request.POST
            p = Person()
            p.first_name = ps.get('first_name')
            p.last_name = ps.get('last_name')
            p.date_of_birth = ps.get('birthdate')
            p.gender = ps.get('gender')
            p.position = ps.get('position')
            p.save()
            return render(request, 'form1/stub.html/',
                {'form': form, 'name': name,})
    else:
            form = PersonForm()
            
    return render(request, 'form1/person.html', {
         'form': form, 
    })         
   
   

def seekperson (request):
    parm1 = Person.objects.all()
    return render(request,'form1/person_list.html/', {"parm1" : parm1})

def login_user(request):
    state = "Please log in below..."
   # print state, request
    username = password = ''
    if request.method == 'POST':
    #    print "Method is POST"
        username = request.POST.get('username')
        password = request.POST.get('password')
        
    #    print username, password, " input parms"
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return redirect('/index/')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
   # else:
    #    print request.method , "is method"
    c = RequestContext(request,{'state':state, 'username': username})

    return render_to_response('form1/login.html', c)


def my_logout (request):
     #   print request.method, " is the method."
     #   print request
        logout(request)
        return render(request,'form1/logout.html')

def stub (request):

    return render(request,'form1/stub.html/')    