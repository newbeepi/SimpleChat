from rest_framework import serializers
from .models import Thread, Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        message = Message.objects.create(**validated_data)
        return message


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        exclude = ['participants']

    participants_list = serializers.ListField(source='get_participants')
