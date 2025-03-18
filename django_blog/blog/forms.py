# Custom Registration View
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationFrom(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']
# Compare this snippet from django_blog/blog/views.py:
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import User
# from django.contrib import messages
# from django import forms
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import views as auth_views
# from .models import UserProfile
# from .forms import ProfileUpdateForm
#
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your account has been updated!')
#             return redirect('profile')
#     else:
#         form = ProfileUpdateForm(instance=request.user)
#
#     context = {
#         'form': form
#     }
#     return render(request, 'registration/profile.html', context)

