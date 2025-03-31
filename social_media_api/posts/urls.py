from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed
from posts.models import CustomUserView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = urlpatterns = [
    path('feed/', user_feed, name='feed'),
    path('User', CustomUserView.as_view(), name='CustomUser')
] + router.urls