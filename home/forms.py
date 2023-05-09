from typing import Any
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
    # def clean_email(self):
    #     email=self.cleaned_data['email'].lower()
    #     try:
    #         user=User.objects.exclude(pk=self.instance.pk).get(email=email)
    #     except User.DoesNotExist:
    #         return email
    #     raise forms.ValidationError(f'Email {email} is already in use.')
    # def clean_username(self):
    #     username=self.cleaned_data['username'].lower()
    #     try:
    #         user=User.objects.exclude(pk=self.instance.pk).get(username=username)
    #     except User.DoesNotExist:
    #         return username
    #     raise forms.ValidationError(f'Username {username} is already in use.')
    # def save(self, commit:True):
    #     user= super(EditProfileForm,self).save(commit=False)
    #     user.username=self.cleaned_data['username']
    #     user.email=self.cleaned_data['email']
    #     user.first_name=self.cleaned_data['first_name']
    #     user.last_name=self.cleaned_data['last_name']
    #     if commit:
    #         user.save()
    #     return user