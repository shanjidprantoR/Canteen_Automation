from django.shortcuts import render,HttpResponse,redirect
from demo.forms import RegistrationForm

# Create your views here.
def landing_view(request):
    return render(request,'landing.html')
def home_view(request):
    return render(request,'home.html')

def login (request):
    return render(request,'login.html')

def register(request):
    if(request.method=='POST'):
        form=RegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('home')
    form=RegistrationForm
    context={
        'registration_form' : form,
    }
    return render(request,'register.html',context)

def team(request):
    return render(request,'team.html')
def about (request):
    return render(request,'about.html')
def instructor (request):
    return render(request,'instructor.html')

def order (request):
    return render(request,'order.html')

def stream (request):
    return render(request,'stream.html')

def payment (request):
    return render(request,'payment.html')
def menu (request):
    return render(request,'menu.html')
def logout (request):
    return render(request,'logout.html')
def others (request):
    return render(request,'others.html')