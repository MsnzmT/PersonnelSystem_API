from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer



class LogoutView(GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data={'message': "Bye!"})



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)