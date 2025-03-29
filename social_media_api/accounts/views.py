from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import LoginSerializer,RegistrationUserserializer,CustomUserserializer

CustomUser = get_user_model()
# generics.GenericAPIView

class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationUserserializer
    permission_classes = [permissions.AllowAny]

class LoginUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class LogoutUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()  # Delete the user's token
        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)

class RetrieveUserView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserserializer
    permission_classes = [permissions.IsAuthenticated]

