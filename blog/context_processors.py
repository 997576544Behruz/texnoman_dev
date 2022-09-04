from .models import *
from taggit.models import Tag
def Category_list(request):
    categorys=Category.objects.all()
    tags=Tag.objects.all()
    return{"categorys":categorys,"tags":tags}
