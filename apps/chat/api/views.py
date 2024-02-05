from rest_framework import viewsets

from apps.chat.api.serializers import MessageSerializer, RoomSerializer
from apps.chat.models import Message, Room


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return self.queryset.filter(room_id=self.kwargs.get('room_pk'))
