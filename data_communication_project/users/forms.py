from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	student_number = forms.CharField()
	firstname = forms.CharField()
	lastname = forms.CharField()
	email = forms.EmailField()


	class Meta:
		model = User
		fields = ['username','firstname','lastname','student_number','email', 'password1','password2']