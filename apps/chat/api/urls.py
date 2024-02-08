from rest_framework_nested.routers import DefaultRouter, NestedSimpleRouter

from apps.chat.api.views import MessageViewSet, RoomViewSet

router = DefaultRouter()
router.register(r"rooms", RoomViewSet)

rooms_router = NestedSimpleRouter(router, r"rooms", lookup="room")

rooms_router.register(r"messages", MessageViewSet, basename="room-messages")

urlpatterns = router.urls + rooms_router.urls
