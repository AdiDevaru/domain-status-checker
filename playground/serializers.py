from rest_framework import serializers
from .models import InitialUrls

class InitialURLsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialUrls
        fields = ['scan_id', 'url', 'flag']


class DomainSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
    domain = serializers.CharField()
    status = serializers.CharField()