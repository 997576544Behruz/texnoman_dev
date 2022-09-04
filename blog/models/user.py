from django.db import models
from django.contrib.auth.models import AbstractUser
class MyUser(AbstractUser):
    bio=models.TextField(blank=True,null=True)
    telegram=models.URLField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to="user/")
    def __str__(self):
        return self.username