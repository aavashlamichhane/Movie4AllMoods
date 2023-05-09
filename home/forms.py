from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from home.models import Profile

class EditProfileForm(ModelForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fname = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    lname = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'username',
        )
