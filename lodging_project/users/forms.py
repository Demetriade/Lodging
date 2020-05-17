from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=32)
    last_name = forms.CharField(required=True, max_length=32)
    email = forms.EmailField(required=True, max_length=64, help_text='Enter a valid email address')
    is_owner = forms.BooleanField(required=False, help_text='Are you owner')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'is_owner', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']