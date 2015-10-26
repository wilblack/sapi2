from django.shortcuts import render

from menu.models import Menu
from menu.serializers import MenuSerializer

from rest_framework import status, viewsets


class MenuViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
