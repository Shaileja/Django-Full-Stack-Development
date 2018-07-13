from django import forms

# Very Basic Example of a Django Form

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


class RegisterForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)
	password=forms.CharField(widget=forms.PasswordInput())
	picture=forms.ImageField()
