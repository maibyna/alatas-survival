from django.forms import ModelForm
from main.models import SurvivalEntry
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SurvivalEntryForm(ModelForm):
    class Meta:
        model = SurvivalEntry
        fields = ["name", "price", "description"]

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')

#     # Override the __init__ method to remove help text
#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#         self.fields['password1'].help_text = None  # Remove password help text
#         self.fields['password2'].help_text = None