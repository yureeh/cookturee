from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = self.fields['first_name'].label or 'Enter Username'
        self.fields['last_name'].widget.attrs['placeholder'] = self.fields['last_name'].label or 'Enter Last Name'
        self.fields['username'].widget.attrs['placeholder'] = self.fields['username'].label or 'Enter Username'
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'Enter Email Address'
        self.fields['password1'].widget.attrs['placeholder'] = self.fields['password1'].label or 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = self.fields['password2'].label or 'Confirm Password'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

        # widgets = {
        #     'username': forms.TextInput(attrs={'placeholder': 'Enter username here'}),
        #     'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address here'}),
        #     'password1': forms.TextInput(attrs={'placeholder': 'Enter Password here'}),
        #     'password2': forms.TextInput(attrs={'placeholder': 'Comfirm PAssword here'}),
        # }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = self.fields['username'].label or 'Enter Username'
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'Enter Email Address'
        self.fields['first_name'].widget.attrs['placeholder'] = self.fields['first_name'].label or 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = self.fields['last_name'].label or 'Enter Last Name'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['propic']
