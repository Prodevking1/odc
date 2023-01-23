from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=70, label="User Name",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'user name'}))
    password = forms.CharField(max_length=70, label="Password",
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'password'}))

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role','phone','profil_photo')