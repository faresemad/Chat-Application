from django.contrib import admin

from apps.chat.models import Message, Room

admin.site.register(Room)
admin.site.register(Message)
