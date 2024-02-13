from django.shortcuts import render
from django.contrib.auth.models import Permission, Group
from auth_mgmt.serializer import (
    PermissionDetailSerializer,
    GroupDetailSerializer,
    GroupPermissionsSerializer
)
from rest_framework import viewsets, status, decorators
from rest_framework.response import Response

class PermissionDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionDetailSerializer
    queryset = Permission.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GroupDetailViewSet(viewsets.ModelViewSet):
    serializer_class = GroupDetailSerializer
    queryset = Group.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, *args, **kwargs):
        group = self.get_object()
        serializer = self.serializer_class(group)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        group = self.get_object()
        serializer = self.get_serializer(group, data=request.data, context={'id': 'pk'})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_message, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        group = self.get_object()
        serializer = self.get_serializer(group, data=request.data, context={'id', 'pk'})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messsage, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        group = self.get_object()
        group.delete()
        return Response({'msg': 'Deleted'}, status=status.HTTP_200_OK)
    
############# ASSIGNING PERMISSIONS TO THE GROUPS AND RETRIEVING THEM #############
    
class GroupPermissonsViewset(viewsets.ModelViewSet):
    serializer_class = GroupPermissionsSerializer
    queryset = Group.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        group = self.get_object()
        serializer = self.get_serializer(group)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        group = self.get_object()
        permissions = request.data["permissions"]
        for perm in permissions:
            perm = Permission.objects.get(codename=perm)
            group.permissions.add(perm)
        serilaizer = self.get_serializer(group)
        return Response(serilaizer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        group = self.get_object()
        permissions = request.data["permissions"]
        for perm in permissions:
            perm = Permission.objects.get(codename=perm)
            group.permissions.remove(perm)
        serilaizer = self.get_serializer(group)
        return Response(serilaizer.data, status=status.HTTP_200_OK)