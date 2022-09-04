from django.contrib.auth.forms import UserCreationForm
from blog.models import MyUser

class RegisterForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=('username','img','email','password1','password2')
        