from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from tokenizer.serializer import TokensListSerializers
from django.contrib.auth import get_user_model

User = get_user_model()

class TokensListViewSet(viewsets.GenericViewSet):
    queryset = Token.objects.all()
    serializer_class = TokensListSerializers

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user_mail = request.data["username"]
        user = User.objects.get(email=user_mail)
        token, created = Token.objects.get_or_create(user=user)
        response = {
            'token': token.key,
            'user': user_mail,
            'created' : created
        }
        return  Response(response, status=status.HTTP_200_OK)