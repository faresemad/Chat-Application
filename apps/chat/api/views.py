from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.chat.api.serializers import MessageSerializer, RoomCUDSerializer, RoomGETSerializer
from apps.chat.models import Message, Room
from apps.utils.permissions import IsOwnerOrReadOnly


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomGETSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]
        elif self.action in ["create"]:
            return [IsAuthenticated()]
        return []

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return RoomCUDSerializer
        return RoomGETSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return self.queryset.filter(room_id=self.kwargs.get('room_pk'))
