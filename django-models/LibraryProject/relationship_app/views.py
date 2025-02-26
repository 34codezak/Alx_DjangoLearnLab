from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books') # Redirect to the list_books view after registration
        
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


#A function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    
def check_admin(user):
    return user.userprofile.role == 'Admin'

def check_librarian(user):
    return user.userprofile.role == 'Librarian'

def check_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')