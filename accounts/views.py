from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import UserRegisterationForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

# def user_register(request):
#     return HttpResponse('Hello User Account')

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)        
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['user'], email=cd['email'], password=cd['password'] )
            messages.success(request, 'User Saved Successfully', 'success')
            # return redirect('hello')

        
    else:
        form = UserRegisterationForm()
    return render(request, 'register.html', {'form' : form})
        
    
    