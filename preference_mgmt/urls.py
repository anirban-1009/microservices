from django.urls import include, path
from rest_framework.routers import DefaultRouter
from preference_mgmt.views import (
    UpdateUserViewSet,
    UpdateCommViewSet,
    UserPermissionsDetailViewSet,
    UserGroupsDetailViewSet
)

router = DefaultRouter()
router.register('user-detail', UpdateUserViewSet, basename='user-detail')
router.register('user-communications', UpdateCommViewSet, basename='user-communications')
router.register('user-permissions', UserPermissionsDetailViewSet, basename='user-permissions-detail')
router.register('user-groups', UserGroupsDetailViewSet, basename='user-groups-detail')

urlpatterns = [
    path('', include(router.urls)),
]