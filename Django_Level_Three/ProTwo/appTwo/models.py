from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=128)	
	email = models.EmailField(max_length=254,unique=True)
	password1=forms.Charfield(widget=forms.PasswordInput()
	password2=forms.Charfield(widget=forms.PasswordInput()
	picture=forms.imageFields()

