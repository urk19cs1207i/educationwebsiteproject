from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app1.forms import EmployeeForm
from app1.models import Employee
from app1.models import Parent
from app1.forms import ParentForm
from app1.forms import Contact 
from app1.forms import ContactForm
from app1.forms import SignupForm  

# Create your views here.

def homeview(request):
    return render(request, "app1/home.html")

def aboutview(request):
    return render(request, "app1/about.html")

def pythonview(request):
    return render(request, "app1/python.html")

def javaview(request):
    return render(request, "app1/java.html")

def djangoview(request):
    return render(request, "app1/django.html")

def mernview(request):
    return render(request, "app1/mern.html")

def photosview(request):
    return render(request, "app1/photos.html")

def videosview(request):
    return render(request, "app1/videos.html")

def latestnewsview(request):
    return render(request, "app1/latestnews.html")



def parentregview(request):
    form = ParentForm()
    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home/')
    return render(request, 'app1/parentReg.html', {'f':form})



def contactview(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home/')
    return render(request, 'app1/contact.html', {'f':form})

def deleteview(request,id):
    data=Parent.objects.get(id=id)
    data.delete()
    return redirect('/home/')

def updateview(request,id):
    f=Parent.objects.get(id=id)
    if request.method == 'POST':
        form=ParentForm(request.POST, instance=f)
        if form.is_valid():
            form.save()
        return redirect('/home/')
    return render(request, 'app1/update.html', {'data': f}) 

def thanksview(request):
    return render(request, "app1/logout.html")

#logout view
def logoutview(request):
    logout(request) 
    return redirect('/thanks/')

#signup view
def signupview(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login/')
    return render(request, 'app1/register.html', {'form':form})


