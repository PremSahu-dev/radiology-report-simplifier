from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .serializers import (
    RegisterSerializer,
    LoginSerializer
)

@method_decorator(csrf_exempt, name="dispatch")
class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message":
                    "User Registered Successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@method_decorator(csrf_exempt, name="dispatch")
class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh":
                str(refresh),

                "access":
                str(refresh.access_token)
            }
        )


class ProfileView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        return Response(
            {
                "id":
                request.user.id,

                "username":
                request.user.username,

                "email":
                request.user.email
            }
        )