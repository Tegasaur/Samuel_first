from django import forms
from app1.models import creditcard
from django.core import validators
class creditforms(forms.ModelForm):
    class Meta():
        model=creditcard
        fields="__all__"
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
