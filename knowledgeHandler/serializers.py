from rest_framework import serializers


class WordSerializer(serializers.Serializer):
    word = serializers.CharField(required=True, max_length=32)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
