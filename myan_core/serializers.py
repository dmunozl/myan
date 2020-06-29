from rest_framework import serializers
from .models import MyanUser


class MyanUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyanUser
        fields = ['id', 'url', 'username', 'email']
