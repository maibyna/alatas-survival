from django.forms import ModelForm
from main.models import SurvivalEntry
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SurvivalEntryForm(ModelForm):
    class Meta:
        model = SurvivalEntry
        fields = ["name", "price", "description"]

<<<<<<< HEAD
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')

#     # Override the __init__ method to remove help text
#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#         self.fields['password1'].help_text = None  # Remove password help text
#         self.fields['password2'].help_text = None


=======
>>>>>>> 295280dd14830525e1259534734d33c72263a24e
