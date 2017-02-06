from django import forms

class UploadFileForm(forms.Form):
	filefield = forms.ImageField()
