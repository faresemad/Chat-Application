from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.chat.models import Message, Room

User = get_user_model()


class BaseUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "full_name"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class UserSerializer(BaseUserSerializer):
    pass


class MemberSerializer(BaseUserSerializer):
    pass


class RoomCUDSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Room
        fields = '__all__'


class RoomRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    members = MemberSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name"]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
