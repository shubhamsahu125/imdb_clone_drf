from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    # making extra field 'password2' for User model using serializer
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        # validation for same password and password2
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'error': 'P1 and P2 should be same!'}
            )
        # validation for unique email
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'error': 'Email already exists!'}
            )
        # create user manually
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        account.set_password(password)
        account.save()
        return account
        

