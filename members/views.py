from django.shortcuts import render
from members.serializers import MemberSerializer, MemberTypeSerializer
from rest_framework import viewsets
from rest_framework import permissions
from members.models import Member, MemberType


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class MemberTypeViewSet(viewsets.ModelViewSet):
    queryset = MemberType.objects.all()
    serializer_class = MemberTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
