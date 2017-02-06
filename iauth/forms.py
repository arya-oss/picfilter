from django import forms
from django.forms import widgets
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm ):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)

class UserProfileForm(forms.ModelForm):
	"""form for extended auth User model"""
	class Meta:
		model = UserProfile
		fields = ('phone','birthdate','gender')
		
class UserImageForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=('picture',)

class ProfileUpdateForm(forms.Form):
	first_name = forms.CharField(required=True, max_length=50, label='First Name')
	last_name = forms.CharField(max_length=50, label='Last Name', required=False)
	birthdate = forms.DateField(required=True, label='Date of Birth')
	email = forms.EmailField(required=True, max_length=50, label='Email')
	phone = forms.CharField(max_length=11, required=True, label='Phone Number')
	gender = forms.CharField(max_length=1, required=True, label='Gender')
	def __unicode__(self):
		return self.first_name