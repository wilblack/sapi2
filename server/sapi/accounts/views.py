from django.shortcuts import render

from accounts.models import Profile
from accounts.serializers import ProfileSerializer

from rest_framework import status, viewsets


class ProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
