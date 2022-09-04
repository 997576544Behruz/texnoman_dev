from django.shortcuts import render,redirect
from .form import RegisterForm
from django.contrib.auth import login
from blog.models import MyUser
# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    context={
        'form':form,
    }
    return render(request,'register.html',context)

def username(request):
    users=MyUser.objects.all()
    username = request.GET.get('search')
    if username:
        users = MyUser.objects.filter(username__icontains = username)
    context={
        "users":users,
    }
    return render(request,"user.html",context)