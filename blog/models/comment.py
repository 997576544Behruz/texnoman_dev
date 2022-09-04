from django.db import models
from .user import MyUser 
from .blog import Blog
class Comment(models.Model):
    blog_id=models.ForeignKey("Blog",on_delete=models.SET_NULL,null=True)
    user_id=models.ForeignKey("MyUser",on_delete=models.SET_NULL,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    text=models.TextField()
    def __str__(self):
        return self.text
