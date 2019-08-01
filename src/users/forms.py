from django import forms
from .models import Role
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['user_role']

## something goes wrong
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
