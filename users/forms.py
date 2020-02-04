from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField() # default validation set to True

    class Meta:
        model = User # Set the form to interact with the User model
        fields = ['username', 'email', 'password1', 'password2'] # Specify the fields made available to the user
        help_texts = {'username':None, 'email':None} # Hide help text from the user and email fields

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget = forms.PasswordInput())

class EmailChangeForm(forms.Form):
    current_email = forms.EmailField(label = 'Current email')
    email1 = forms.EmailField(label = 'New email')
    email2 = forms.EmailField(label = 'New email confirm')

    class Meta:
        model = User
        fields = ['email']
    
    