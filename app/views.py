from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import resume_form,RegistrationForm,ResumeList
from .models import profile
import pdfkit
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        about=request.POST.get('about')
        college=request.POST.get('college')
        degree=request.POST.get('degree')
        project=request.POST.get('project')

        pr1 = profile(
            name = name,
            email = email,
            about = about,
            college = college,
            degree = degree,
            project = project
        )
        pr1.save()
        return HttpResponse('Generation successful')
    context={
        "form" : resume_form()
    }
    return render(request,'index.html',context)

@login_required
def view_resume(request, id):
    pr_details=profile.objects.get(id=id)
    context={
        "id":id,
        "name" : pr_details.name,
        "email" :pr_details.email,
        "about" : pr_details.about,
        "college" : pr_details.college,
        "degree" : pr_details.degree,
        "project" : pr_details.project
    }
    return render(request,'display.html',context)

def download(request,id):
    pr_details=profile.objects.get(id=id)
    context={
        "id" : id,
        "name" : pr_details.name,
        "email" :pr_details.email,
        "about" : pr_details.about,
        "college" : pr_details.college,
        "degree" : pr_details.degree,
        "project" : pr_details.project
    }
    template=loader.get_template('display.html')
    html = template.render(context)
    options = {
        'page-size' : 'Letter',
        'encoding' :"UTF-8"
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    return response

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse("Invalid data")
    form=RegistrationForm()
    return render(request,"register.html",{"form":form})

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            form=login(request, user)
            messages.success(request,f'Login Successful !!')
            return redirect('index')
    form = AuthenticationForm()
    return render(request,'login.html',{"form":form})
@login_required
def logout(request):
    auth_logout(request)
    messages.success(request,f'Logout Successful !!')
    return redirect("login")
@login_required
def resume_list(request):
    if request.method=='POST':
        id= request.POST.get('resume_id')
        return view_resume(request,id=id)
    return render(request,'resume_list.html',{'form': ResumeList()})