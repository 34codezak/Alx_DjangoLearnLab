from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
from .models import Notification

class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

from django.http import JsonResponse
def follow_user(request):
    return JsonResponse({"message": "Follow user functionality"})

def unfollow_user(request):
    return JsonResponse({"message": "Unfollow user functionality"})

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_to_follow = CustomUser.objects.get(id=kwargs.get("user_id"))
        request.user.following.add(user_to_follow)
        return Response({"message": "User followed successfully"})
