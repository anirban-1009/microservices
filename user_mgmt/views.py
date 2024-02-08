from rest_framework.response import Response
from rest_framework import viewsets, status
from User.models import User
from user_mgmt.serializers import UsersSerializer
from rest_framework.views import APIView
import requests
from django.urls import reverse

base_url = 'http://localhost:8000/'
class UsersListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UsersDetailViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response({'msg': 'Deleted'}, status=status.HTTP_200_OK)
    
class LoginAPIView(APIView):
    def post(self,request):
        user = request.data.get('username')
        password = request.data.get('password')

        token_post_url = f'{base_url}token/list/'
        payload = {
            'username': user,
            'password': password
        }
        response = requests.post(token_post_url,payload)
        if response.status_code == 200:
            token = response.json().get('token')
            request.session['token'] = token
            return Response({'token': token}, status=status.HTTP_200_OK)
        return Response({'msg', 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

class LogOutAPIView(APIView):
    def post(self, request):
        if request.session['token']:
            token = request.session['token']
            token_del_url = f'{base_url}/token/detail/{token}/'
            response = requests.delete(token_del_url)
            if response.status_code == 200:
                del request.session['token']
                return Response({'msg': f'logged out of {token}'}, status=status.HTTP_200_OK)
            return Response({'msg': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)