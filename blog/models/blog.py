from django.db import models
from django_quill.fields import QuillField
from taggit.managers import TaggableManager
from .category import Category
from .user import MyUser
class Blog(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=50,unique=True)
    content=QuillField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    img=models.ImageField(upload_to="blogs/")
    category=models.ForeignKey("Category",on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey("MyUser",on_delete=models.SET_NULL,null=True)
    views_count=models.BigIntegerField(default=0)
    user_count=models.IntegerField(default=0)
    tags=TaggableManager()
    def __str__(self):
        return self.title