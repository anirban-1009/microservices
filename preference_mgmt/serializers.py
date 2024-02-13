from rest_framework import serializers
from User.models import User

class UserPreferenceUpdateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name', 'gender']

class UserCommPreferenceUpdateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['preferred_language', 'receive_notifications']

class UserPermissionsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_permissions']

class UserGroupsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['groups']