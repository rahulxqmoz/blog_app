from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)  # Confirmation password

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True) 
    class Meta:
        model = Post
        fields = ['id', 'user','title', 'content', 'image', 'created_at', 'updated_at']

    def validate(self, attrs):
        """
        Add custom validation logic if needed (e.g., checking that content is not empty).
        """
        # Example of validating that content is not empty
        if not attrs.get('content'):
            raise serializers.ValidationError("Content cannot be empty.")
        return attrs

    def create(self, validated_data):
        """
        Custom create method to ensure the user is set when creating a post.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Custom update method, ensuring the user can't change ownership of the post.
        """
        if validated_data.get('user') and validated_data['user'] != instance.user:
            raise serializers.ValidationError("You cannot change the post's user.")
        return super().update(instance, validated_data)

