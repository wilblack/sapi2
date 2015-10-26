
from accounts.models import Profile, Org

from utils import JSONSerializer



from rest_framework import serializers


class OrgSerializer(serializers.ModelSerializer):
    attrs = JSONSerializer()
    partial = True

    class Meta:
        model = Org
        fields = ('name', 'slug', 'attrs')


class ProfileSerializer(serializers.ModelSerializer):
    org = OrgSerializer()
    username = serializers.ReadOnlyField(source='user.username')
    attrs = JSONSerializer()

    class Meta:
        model = Profile
        fields = ('username', 'attrs', 'org')


