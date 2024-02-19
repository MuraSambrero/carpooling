from .models import Trip, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        exclude = ('id', 'owner')
