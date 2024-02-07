from tokenizer.auth import BearerAuthentication
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from tokenizer.serializer import TokensListSerializers

class TokensListViewSet(viewsets.GenericViewSet):
    queryset = Token.objects.all()
    serializer_class = TokensListSerializers

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)