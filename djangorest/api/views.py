from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from .permissions import IsOwner, IsStaffOrTargetUser
from .serializers import BucketlistSerializer, ItemSerializer, UserSerializer
from .models import Bucketlist, Item


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (permissions.AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BucketlistView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Bucketlist.objects.all()
        queryset = queryset.filter(owner=self.request.user)
        q = self.request.query_params.get('q', '')
        if q is not None:
            queryset = queryset.filter(name__icontains=q)
        return queryset


class BucketlistDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)


class ItemView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new item."""
        bucketlist = Bucketlist.objects.get(pk=self.kwargs['pk'])
        serializer.save(owner=self.request.user, bucketlist=bucketlist)


class ItemsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)
