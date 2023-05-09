from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate

from home.models import Profile

class EditProfileForm(forms.ModelForm):
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username= forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
        )