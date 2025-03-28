from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = CustomUser.objects.filter(username=serializer.validated_data["username"]).first()
        if user in user.check_password(serializer.validated_data["password"]):
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        return Response({"error": "Invalid data"}, status=400)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
