from django.shortcuts import render
from django.contrib.auth.models import Permission, Group
from auth_mgmt.serializer import PermissionDetailSerializer, GroupDetailSerializer
from rest_framework import viewsets, status
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
        return Response(serializer.data[0], status=status.HTTP_200_OK)
    
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