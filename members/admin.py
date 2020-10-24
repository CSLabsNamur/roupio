from django.contrib import admin
from members.models import Member, MemberType

# Register your models here.
admin.site.register(MemberType)
admin.site.register(Member)