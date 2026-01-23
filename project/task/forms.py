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
#class signupForm(ModelForm):
    #class Meta:
        #model=hello
        #fields='__all__'
class signupForm(forms.ModelForm):
    class Meta:
        model = hello
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.RadioSelect(),
            'dept': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'roll': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'pin': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'mode': forms.RadioSelect(),
        }
