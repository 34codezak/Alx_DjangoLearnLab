from django.urls import path
from . import views, PostByTagListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/comments/new/'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete-comment'),
    path('search/', views.search, name='search'),
    path('tags/<str:tag>/', views.posts_by_tag, name='posts-by-tag'),
    path("tags/<slug:tag_slug>/", PostByTagListViews.as_view(), name='posts-by-tag'),
]