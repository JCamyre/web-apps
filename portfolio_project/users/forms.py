from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		# Basically this is saying from the user inputed data from the form we want to make a User class, with the fields listed
		model = User
		fields = ['username', 'email', 'password1', 'password2']