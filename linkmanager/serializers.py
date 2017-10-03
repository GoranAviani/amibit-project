from rest_framework import serializers
from linkmanager.models import Link,Note

class LinkSerializer(serializers.Serializer):
    class Meta:
        model = Link
        fields = '__all__'
