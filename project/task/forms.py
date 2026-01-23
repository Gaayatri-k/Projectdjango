from datetime import date
from django import forms
from django.forms import ModelForm
from .models import hello
from django.utils.timezone import now
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
            'dob': forms.DateInput(attrs={'type': 'date', 'max': now().date()}),
            'gender': forms.RadioSelect(),
            'year': forms.Select(),
            'address': forms.Textarea(attrs={'rows': 3}),
            'mode': forms.Select(),
        }
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Name must contain at least 3 characters")
        return name
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not mobile.isdigit():
            raise forms.ValidationError("Mobile number must contain only digits")
        if len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be exactly 10 digits")
        return mobile
    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if dob and dob>now().date():
            raise forms.ValidationError("Date of Birth cannot be a future date")
        return dob