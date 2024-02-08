from rest_framework import serializers
from User.models import User

class UserPreferenceUpdateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name']