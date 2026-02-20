from django import forms
from django.forms import ModelForm
from .models import Student
import datetime

class StudentForm(ModelForm):

    skills=forms.MultipleChoiceField(
        choices=[
            ('Python','Python'),
            ('Java','Java'),
            ('C','C'),
            ('WebDev','WebDev')
        ],
        widget=forms.CheckboxSelectMultiple
    )

    agree=forms.BooleanField()

    class Meta:
        model=Student
        fields='__all__'
        exclude=['skills']
        widgets={
            'dob':forms.DateInput(attrs={'type':'date'}),
            'address':forms.Textarea(attrs={'rows':3}),
        }

    def clean_name(self):
        n=self.cleaned_data['name']
        if len(n)<3:
            raise forms.ValidationError("Min3Chars")
        return n

    def clean_mobile(self):
        m=self.cleaned_data['mobile']
        if not m.isdigit() or len(m)!=10:
            raise forms.ValidationError("Mobile10Digits")
        return m

    def clean_dob(self):
        d=self.cleaned_data['dob']
        if d>datetime.date.today():
            raise forms.ValidationError("FutureDateNotAllowed")
        return d
