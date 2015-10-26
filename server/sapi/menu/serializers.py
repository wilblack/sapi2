from utils import JSONSerializer


from menu.models import Menu, MenuItem

from rest_framework import serializers


class MenuItemSerializer(serializers.ModelSerializer):
    attrs = JSONSerializer()
    
    class Meta:
        model = MenuItem
        fields = ('sid', 'name', 'about', 'attrs')


class MenuSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, source='menuitems')

    class Meta:
        model = Menu
        fields = ('id', 'name', 'source', 'items')

