from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','created_at']
    prepopulated_fields={'slug':('name',)}
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['blog_id','user_id','created_at']

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display=['username','first_name','bio']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','created_at','category','user']
    prepopulated_fields={'slug':('title',)}