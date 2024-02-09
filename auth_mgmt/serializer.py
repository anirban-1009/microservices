from rest_framework import serializers
from django.contrib.auth.models import Permission, Group

class PermissionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['name', 'content_type', 'codename']

class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']