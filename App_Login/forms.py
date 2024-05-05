from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'description', 'dob', 'facebook', 'website']

    widgets = {
        'dob': forms.DateInput(attrs={'type': 'date'}),
        'facebook': forms.URLInput(),
        'website': forms.URLInput(),
    }
