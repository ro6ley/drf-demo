from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Bucketlist, Item


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Bucketlist Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'items', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class ItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Item Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Item
        fields = ('id', 'name', 'owner', 'bucketlist', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the User model"""
    bucketlists = serializers.PrimaryKeyRelatedField(many=True, queryset=Bucketlist.objects.all())

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bucketlists')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
