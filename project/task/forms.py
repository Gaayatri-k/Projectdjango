from django import forms
from django.forms import ModelForm
from .models import hello
# class signupForm(forms.Form):
#     username=forms.CharField(
#         label='Enter your name',
#         min_length=8,
#          error_messages={
#             "required":"please enter your name",
#             "min_length":"Enter atleast 8 characters",
#         }
#     )
class signupForm(ModelForm):
    class Meta:
        model=hello
        fields='__all__'