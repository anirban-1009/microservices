from django.shortcuts import render
from rest_framework import viewsets, status
from User.models import User
from preference_mgmt.serializers import UserPreferenceUpdateSerialzier
from tokenizer.auth import BearerAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UpdateUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPreferenceUpdateSerialzier
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
