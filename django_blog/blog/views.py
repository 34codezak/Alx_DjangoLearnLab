from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import UserProfile, Post
from .forms import ProfileUpdateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class PostListView(ListView):
    model = Post
    template_name = 'blog/base.html' # Path to the template
    context_object_name = 'posts'
    ordering = ['-date_posted'] # Order the posts by date posted
    
class PostDetailView(DetailView):    
    model = Post
    template_name = 'blog/post_detail.html' # Path to the template

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html' # Path to the template
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html' # Path to the template
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html' # Path to the template
    success_url = reverse_lazy('home')      
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author