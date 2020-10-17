from django import forms
from django.contrib.auth.models import User
from acubook.models import UserProfileInfo,BookInfo
from django.core import validators

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta():
		model = User
		fields = ('username','email','password')

		widgets = {
			'username' : forms.TextInput(attrs={'class':'form-control'}),
			'email' : forms.EmailInput(attrs={'class':'form-control','required':'required',
												'placeholder':'a@gmail.com'}),
		}
		help_texts = {
			'username':None
		}

	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError('password and confirm_password do not match')





