from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False, unique=True)
    discord = models.CharField(max_length=255, blank=True, unique=True)
    address = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    street_number = models.CharField(max_length=64, blank=False)
    phone_number = models.CharField(max_length=255, blank=True)


class MemberType(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(max_length=512, blank=False)
