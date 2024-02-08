from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from tokenizer.serializer import TokensListSerializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()

def password_check(user, password):
    user = User.objects.get(email=user)
    return check_password(password, user.password)

class TokensListViewSet(viewsets.GenericViewSet):
    queryset = Token.objects.all()
    serializer_class = TokensListSerializers

    def list(self, request):# returns list of tokens with all detailed information
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request): #takes in username and password
        user_mail = request.data["username"]
        password = request.data["password"]
        user = User.objects.get(email=user_mail)
        if password_check(user_mail, password):
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

    def retrieve(self, request, pk=None):# returns {key, user, created_at}
        response = self.serializer_class(self.get_object())
        return Response(response.data,status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        token = self.get_object()
        user = request.data["username"]
        pwd = request.data["password"]
        if password_check(user, pwd):
            token.delete()
            user= User.objects.get(email=user)
            token, created = Token.objects.get_or_create(user=user)
            response = {
                'token': token.key,
                'user': user.email,
                'created' : created,
                'created_at': token.created
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response({'msg': 'UnAuthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def destroy(self, request, *args, **kwargs):
        token = self.get_object()
        token.delete()
        return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)