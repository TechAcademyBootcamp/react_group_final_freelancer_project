from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import *


class RegisterForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta():
        model=CustomUser
        fields=['first_name','last_name','email','username','password1','password2']

class LoginForm(AuthenticationForm):
    username=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta():
        model=CustomUser
        fields='__all__'

# class ProfileForm(forms.ModelForm):
#     def clean_regions(self):
#         regions = self.cleaned_data['regions']
#         if len(regions) > 5:
#             raise forms.ValidationError('You can add maximum 5 skills')
#         return regions

#     class Meta:
#         model = CustomUser
#         fields = '__all__'




# EDIT PROFILE 

class ProfileForm(forms.ModelForm):
    first_name=forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name=forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Last name'}))

    class Meta():
        model=CustomUser
        fields=['first_name','last_name','hourly_price','title','overview']

        widgets={
            'title':forms.TextInput(attrs={
                'placeholder':"Enter your title"
            }),
            'overview':forms.Textarea(attrs={
                'placeholder':"Enter your overview"
            }),
        }

