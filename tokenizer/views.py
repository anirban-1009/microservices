from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from tokenizer.serializer import TokensListSerializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

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
        pwd = request.data["password"]
        if check_password(pwd, user.password):
            token, created = Token.objects.get_or_create(user=user)
            response = {
                'token': token.key,
                'user': user_mail,
                'created' : created,
                'created_at': token.created
            }
            return  Response(response, status=status.HTTP_200_OK)
        return Response({'msg': 'UnAuthotized'}, status=status.HTTP_401_UNAUTHORIZED)
    
class TokensDetailViewSet(viewsets.ModelViewSet):
    serializer_class = TokensListSerializers
    queryset = Token.objects.all()

    def retrieve(self, request, pk=None):
        response = self.serializer_class(self.get_object())
        return Response(response.data,status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        token = self.get_object()
        user = request.data["username"]
        pwd = request.data["password"]
        if str(user)==str(token.user) and check_password(pwd, ):
            # token.delete()
            return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'UnAuthorized'}, status=status.HTTP_401_UNAUTHORIZED)