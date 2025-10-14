from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})