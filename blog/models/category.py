from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True)
    img=models.ImageField(upload_to="Category/")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name