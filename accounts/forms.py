from .models import *
from django.forms import ModelForm
# from django.shortcuts import HttpResponse
from django import forms
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ["username", "email", "text"]


    def save(self,commit=True):
        user = super(PostForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.text = self.cleaned_data['text']

        if commit:
            user.save()

        return user
