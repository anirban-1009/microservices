from django.shortcuts import render
from rest_framework import viewsets, status
from User.models import User
from preference_mgmt.serializers import (
    UserPreferenceUpdateSerialzier,
    UserCommPreferenceUpdateSerialzier,
    UserPermissionsDetailSerializer,
    UserGroupsDetailSerializer
)
import requests
from tokenizer.auth import BearerAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UpdateUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPreferenceUpdateSerialzier
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        token = request.headers["Authorization"][7:]
        url=f"http://localhost:8000/token/detail/{token}"
        response = requests.get(url)
        response = response.json()["user"]
        user = self.serializer_class(self.queryset.get(id=response))
        return Response(user.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateCommViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCommPreferenceUpdateSerialzier
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        token = request.headers["Authorization"][7:]
        url=f"http://localhost:8000/token/detail/{token}"
        response = requests.get(url)
        response = response.json()["user"]
        user_comm = self.serializer_class(self.queryset.get(id=response))
        return Response(user_comm.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        user_comm = self.get_object()
        serializer = self.serializer_class(user_comm, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class UserPermissionsDetailViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPermissionsDetailSerializer
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        token = request.headers["Authorization"][7:]
        url=f"http://localhost:8000/token/detail/{token}"
        response = requests.get(url)
        response = response.json()["user"]
        permission = self.serializer_class(self.queryset.get(id=response))
        return Response(permission.data, status=status.HTTP_200_OK)

class UserGroupsDetailViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserGroupsDetailSerializer
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        token = request.headers["Authorization"][7:]
        url=f"http://localhost:8000/token/detail/{token}"
        response = requests.get(url)
        response = response.json()["user"]
        group = self.serializer_class(self.queryset.get(id=response))
        return Response(group.data, status=status.HTTP_200_OK)