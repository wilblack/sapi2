import uuid

from django.db import models

from rest_framework import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


from accounts.serializers import ProfileSerializer


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


def make_uuid():
    return str(uuid.uuid4())


# Override ObtainAuthToken to also return the username
class ObtainAuthTokenAndProfile(ObtainAuthToken):
    """
        Returns

        {
            'token': API Token,
            'username': Account username,
            'profile': {
                'firstName':'',
                'lastName': '',
                'orgs': [],
                'perms':[
                ]
            }
        }
    """



    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # # Account into
        request.data.update({'preferences':{'wtf':''}})
        request.data.update({'user':user.id})
        
        profile = ProfileSerializer(user.profile)
        
        token, created = Token.objects.get_or_create(user=user)

        accountInfo = {
            'token': token.key,
            'username':user.username,
            'profile': profile.data
        }
        return Response(accountInfo)




def get_org_queryset(self):
    user = self.request.user
    orgSlug = self.request.query_params.get("orgSlug", None)
    user_org = None

    if user.is_staff:
        if orgSlug:
            org = Org.objects.get(slug=orgSlug)
            qs = self.queryset.filter(org=org)
        else:
            qs = self.queryset.all()
        return qs
    else:

        if user.profile.orgs.all():
            user_org = user.profile.orgs.all()[0]

        if user.groups.filter(name__in=['Organization Staff', 'Organization Admin']).exists():
            qs = self.queryset.filter(org=user_org)
        else:
            return self.queryset.none()

        if orgSlug and (not orgSlug == user_org.slug):
            
            return self.queryset.none()
        return qs