from django import forms


class UserRegisterationForm(forms.Form):
    user = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    
    