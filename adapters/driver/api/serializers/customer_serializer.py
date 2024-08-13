from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    cpf = serializers.CharField(max_length=11)
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()