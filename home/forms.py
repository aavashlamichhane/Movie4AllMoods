from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate

from home.models import Profile

class EditProfileForm(UserChangeForm):
    fname= forms.CharField(widget=forms.TextInput(attrs={'class':'form_control','placeholder':'{{user.first_name}}'}))
    lname= forms.CharField(widget=forms.TextInput(attrs={'class':'form_control','placeholder':'{{user.last_name}}'}))
    username = forms.CharField(max_length=30,widget=forms.EmailInput(attrs={'class':'form_control','placeholder':'{{user.username}}'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form_control','placeholder':'{{user.email}}'}))
    
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'username',
        )