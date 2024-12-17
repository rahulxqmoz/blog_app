from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from .serializers import RegisterSerializer
from rest_framework import generics, permissions,status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth import authenticate
# Create your views here.



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Save and retrieve the created user
        refresh = RefreshToken.for_user(user)  # Generate tokens for the user

        # Return the user data along with tokens
        response_data = {
            "user": serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(response_data)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generate JWT tokens for the authenticated user
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "date_joined":user.date_joined,
                },
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return only the posts created by the authenticated user.
        """
        user_param = self.request.query_params.get('user', None)
        if user_param:
            return self.queryset.filter(user__id=user_param).order_by('-created_at')
        return self.queryset.order_by('-created_at')


    def perform_create(self, serializer):
        """
        Save the post instance with the authenticated user.
        """
        serializer.save(user=self.request.user)