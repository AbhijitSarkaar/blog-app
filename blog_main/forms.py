from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from blogs.models import Comment


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('email', 'username', 'password1', 'password2')

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)