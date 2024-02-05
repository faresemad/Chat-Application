from rest_framework import serializers

from apps.chat.models import Message, Room


class RoomSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Room
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
