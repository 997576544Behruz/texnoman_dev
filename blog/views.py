from django.shortcuts import render,redirect
from blog.forms import BlogForm,CommentForm
from .models import *
from taggit.models import Tag
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.paginator import Paginator 
from blog.models import Blog,MyUser

from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
# Create your views here.
@login_required(login_url="login_page")
def add_blog(request):
    form= BlogForm()
    if request.method=="POST":
        form =BlogForm(request.POST,request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user
            f.slug=slugify(f.title)
            f.save()
            form.save_m2m()
            return redirect("home")
    context={
        "form":form,
    }
    return render(request,"add_blog.html",context)

@login_required(login_url="login_page")
def update_blog(request,slug):
    blog=Blog.objects.get(slug=slug)
    form = BlogForm(instance=blog)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            tags=Tag.objects.all()
            for tag in tags:
                blogss=Blog.objects.filter(tags=tag).exists()
                if not blogss:
                    tag.delete()
            return redirect('more_news', slug=blog.slug)
    context={
        "blog":blog,
        'form':form
    }
    return render(request,"update_blog.html",context)
@login_required(login_url="login_page")
def delete_blog(request,slug):
    blog=Blog.objects.get(slug=slug)
    if request.method == "POST":
        tags = blog.tags.all()
        for tag in tags:
            t = Tag.objects.get(name=tag.name)
            t.delete()
        blog.delete()
        return redirect('home')
    context={
        "blog":blog,
    }
    return render(request,"delete_blog.html",context)


def home1(request):
    blogs=Blog.objects.all()
    p = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    title = request.GET.get('search')
    if title:
        blogsearch = Blog.objects.filter(title__icontains = title)
        print(blogsearch) 
    context={
        'blogs':page_obj,
        # 'blogsearch':blogsearch,
    }
    return render(request,"home.html",context)
def more_news(request,slug):
    blog=Blog.objects.get(slug=slug)
    # user=MyUser.objects.get()
    form=CommentForm()
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.blog_id=blog
            f.user_id=request.user
            f.save()
            return redirect('more_news',slug=blog.slug)
    blog.views_count+=1
    blog.save()
    context={
        'blog':blog,
        'form':form,
    }
    return render(request,"more.html",context)
def tag(request,slug):
    tag = Tag.objects.get(slug=slug)
    blogs=Blog.objects.filter(tags=tag)
    context={
        "tag":tag,
        "blogs":blogs,
        }
    return render(request,"tag.html",context)
def Categorys(request,slug):
    category=Category.objects.get(slug=slug)
    blogs=Blog.objects.filter(category=category)
    context={
        "category":category,
        "blogs":blogs,
    }
    return render(request,"Category.html",context)
def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"password or username error")
            return redirect('login_page')
    return render(request,"login.html")
def log_out(request):
    logout(request)
    return redirect('login_page')
