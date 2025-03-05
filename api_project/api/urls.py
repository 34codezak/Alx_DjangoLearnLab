from django.urls import path
from .views import BookList
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'), # Maps to the BookList view
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Endpoint to obtain the token
]