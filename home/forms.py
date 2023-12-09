from django import forms
from .models import Todo


class CreateTodoForms(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()
    

class UpdateTodoForms(forms.ModelForm):   #Model_Based Form
    class Meta:
        model=Todo
        fields="__all__" #همه رو بردار بیار   
    
    
    