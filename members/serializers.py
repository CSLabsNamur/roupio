from rest_framework import serializers
from members.models import Member, MemberType


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'surname', 'email', 'discord',
                  'address', 'city', 'street_number', 'phone_number']


class MemberTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MemberType
        fields = ['id', 'name', 'description']
