from rest_framework import serializers
from django.utils import timezone
from backstage.models import Member

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'