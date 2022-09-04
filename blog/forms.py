from dataclasses import field
from django import forms
from blog.models import Blog,Comment
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','img','category','content','tags')
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('text',)