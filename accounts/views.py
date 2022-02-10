from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.decorators import login_required

def signin(request):
    return render(request,'accounts/signin.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})