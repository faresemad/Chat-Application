import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    online = models.ManyToManyField(User, related_name='rooms')

    def __str__(self):
        return self.name

    def get_online_count(self):
        return self.online.count()

    def join_room(self, user):
        self.online.add(user)

    def leave_room(self, user):
        self.online.remove(user)


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
