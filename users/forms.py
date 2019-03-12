from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

#forms
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'first_name', 'last_name',
            'email', 'username',
            'gender', 'age',
            'memory', 'country',
            'about',
        )
          
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name',
            'email', 'username',
            'gender', 'age',
            'memory', 'country',
            'about',
        )