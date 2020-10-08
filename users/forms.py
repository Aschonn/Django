#forms import
from django import forms
from django.contrib.auth.forms import UserCreationForm
#models import
from django.contrib.auth.models import User
from .models import Profile, Feedback



class UserRegisterForm(UserCreationForm):
    #adding new email field to usercreationform
    email = forms.EmailField()

    class Meta:
        #Which model/table do we want to toggle/use
        model = User
        #fields that will be shown
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['username', 'email', 'comments']