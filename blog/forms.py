from .models import Comment
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.conf import settings
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class EditProfileForm(UserChangeForm):
    password = None
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    is_superuser = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "is_superuser"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "is_superuser": forms.CheckboxInput(attrs={"class": "form-check"})
        }
