from django.urls import path
from .views import *
urlpatterns=[
    path('',home1,name="home"),
    path('news/<slug:slug>',more_news,name="more_news"),
    path('tag/<slug:slug>',tag,name="tag"),
    path('Category/<slug:slug>',Categorys,name="Categorys"),
    path('user/',login_page,name="login_page"),
    path('logout/',log_out,name="log_out"),
    path("add_blog/",add_blog,name="add_blog"),
    path('delete_blog/<slug:slug>',delete_blog,name="delete_blog"),
    path('update_blog/<slug:slug>',update_blog,name="update_blog"),
]