from django.urls import path, include
from rest_framework import routers
from .viewsets import DashboardViewSet, BoardViewSet, CardViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'dashboard', DashboardViewSet)
router.register(r'board', BoardViewSet)
router.register(r'card', CardViewSet)
router.register(r'comment', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]