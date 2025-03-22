from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import User
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import UserProfile, Post, Comment
from .forms import ProfileUpdateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from taggit.models import Tag
from django.views.generic.list import ListView

def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

def register(request):
    return render(request, 'blog/register.html')

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
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html' # Path to the template
    success_url = reverse_lazy('home')      
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html' # Path to the template
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk']})
    
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html' # Path to the template
    
class CommentDeleteView(DeleteView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_confirm_delete.html' # Path to the template