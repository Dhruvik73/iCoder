from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from blog.models import blogpost
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    blogs=blogpost.objects.all()
    params={'blogs':blogs}
    return render(request,'home/home.html',params)
def about(request):
    return render(request,'home/about.html')
def contacts(request):
    if request.method=='POST':
       name=request.POST.get('name')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       query=request.POST.get('query')
       if len(name)<3 or len(email)<8 or len(phone)!=10 or len(query)<3:
           messages.error(request, 'Please Fill Form Correctly')
       else:
        Contact=contact(name=name,email=email,phone=phone,query=query)
        Contact.save()
        messages.success(request, 'Your Contact Details Was Submited!👍😁')
    return render(request,'home/contact.html')
def search(request):
    query=request.GET['query']
    if(len(query)>78):
        blogs=[]
    else:
        blogstitle=blogpost.objects.filter(title__icontains=query)
        blogscontent=blogpost.objects.filter(content__icontains=query)
        blogs=blogstitle.union(blogscontent)
    params={'blogs':blogs,'query':query}
    return render(request,'home/search.html',params)
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        #check....
        if len(username)>10:
            messages.error(request, 'username must be under 10 char...')
            return redirect('home')
        if not username.isalnum():
            messages.error(request, 'username must contain alphanumaric char...')
            return redirect('home')
        if pass1[0:len(username)] in username or len(pass1)<8:
               messages.error(request, 'enter strong password')
               return redirect('home')
        if pass1!=pass2:
            messages.error(request, 'passwrod must be same')
            return redirect('home')
        myuser=User.objects.create(username=username,email=email,)
        myuser.password=pass1
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, 'your icoder account created successfully')
        return redirect('home')
        #home is name of our url path for more go to home urls folder
    else:
        return HttpResponse('error -404 NOT FOUND')


def Login(request):
        if request.method=='POST':
         loginusername=request.POST['lusername']
         loginpassword=request.POST.get('lpassword')

         user=authenticate(username=loginusername,password=loginpassword)
         if user is not None:
             login(request,user)
             messages.success(request, 'you are loged in')
             return redirect('home')
         else:
             messages.error(request, 'enter valid details')
             return redirect('home')
        else:
            return HttpResponse('error -404 NOT FOUND')

def Logout(request):
    logout(request)
    messages.success(request, 'logedout')
    return redirect('home')

