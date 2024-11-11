from rest_framework import serializers

class DomainSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
    domain = serializers.CharField()
    status = serializers.CharField()