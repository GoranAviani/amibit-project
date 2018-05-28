from rest_framework import serializers
from linkmanager.models import Link,Note
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
        )

class LinkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        #fields = '__all__'
        fields = (
        'link_name',
        'link_url',
        )
