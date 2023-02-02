from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']


class UserUpdateform(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=500)
    last_name = forms.CharField(max_length=500)

    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    

    class Meta:
        model = Profile
        fields = ['avatar']