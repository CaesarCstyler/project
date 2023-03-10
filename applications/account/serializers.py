from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from applications.account.send_email import send_activation_code

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        required=True,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User 
        fields = ('username', 'email', 'password', 'password2')


    def validate_email(self, email):
        return email

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Passwords did not match!')

        return attrs


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            return email
        raise serializers.ValidationError('User not found')

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')


        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError('Incorrect password')
        attrs['user'] = user
        return attrs
