from django.urls import path
from .views import RegisterView, LoginView, ProfileView, follow_user, unfollow_user
from accounts.views import FollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]