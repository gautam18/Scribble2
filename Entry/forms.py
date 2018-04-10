from django.contrib.auth.models import User
from .models import Profile
from django import forms

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model=User
		fields=['username','email','password']


	



class LoginForm(forms.Form):

	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)