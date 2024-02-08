from django.urls import include, path
from rest_framework.routers import DefaultRouter
from preference_mgmt.views import UpdateUserViewSet, UpdateCommViewSet

router = DefaultRouter()
router.register('user-detail', UpdateUserViewSet, basename='user-detail')
router.register('user-communication', UpdateCommViewSet, basename='user-communication')

urlpatterns = [
    path('', include(router.urls)),
]