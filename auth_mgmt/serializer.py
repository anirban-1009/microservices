from rest_framework import serializers
from django.contrib.auth.models import Permission, Group

class PermissionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['name', 'content_type', 'codename', 'id']

class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class GroupPermissionsSerializer(serializers.ModelSerializer):
    permissions = PermissionDetailSerializer(many=True, required=False)

    class Meta:
        model: Group = Group
        fields = [f.name for f in model._meta.fields]
        fields.append('permissions')