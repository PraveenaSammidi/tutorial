from rest_framework import serializers
from .models import Members


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'
