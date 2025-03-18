from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import UserProfile
from .forms import ProfileUpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    context = {
        'form': form
    }
    return render(request, 'registration/profile.html', context)