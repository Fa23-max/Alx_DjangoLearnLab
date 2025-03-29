from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model,authenticate
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password



class CustomUserserializer(serializers.ModelSerializer):
    class Meta:
        model  = get_user_model()
        fields = "__all__"


class RegistrationUserserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6, validators=[validate_password])
    class Meta:
        model  = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']
        
    def create(self,validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )
        Token.objects.create(user=user)  # Create token for new user
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        token, created = Token.objects.get_or_create(user=user)
        return {"token": token.key, "user": CustomUserserializer(user).data}


