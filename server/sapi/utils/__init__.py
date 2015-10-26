from rest_framework import serializers


class JSONSerializer(serializers.Field):
    """
    A serialiizer for JSONField fields.
    """
    def to_native(self, obj):
        return obj

    def to_internal_value(self, obj):
        return obj

    def to_representation(self, instance):
        return instance