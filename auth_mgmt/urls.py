from django.urls import include, path
from rest_framework.routers import DefaultRouter
from auth_mgmt.views import (
    PermissionDetailViewSet,
    GroupDetailViewSet,
    GroupPermissonsViewset
)

router = DefaultRouter()
router.register('permission-list', PermissionDetailViewSet, basename='permission-list')
router.register('group', GroupDetailViewSet, basename='group-detail')
router.register('group/permissions', GroupPermissonsViewset, basename='group-detail-permissions')

urlpatterns = [
    path('', include(router.urls)),
    # Include the viewset itself for 'group-detail' endpoint
    path('groups/', GroupDetailViewSet.as_view({'get': 'list', 'post': 'create'}), name='group-list'),
    path('permissions/', GroupPermissonsViewset.as_view({'get': 'list', 'post': 'create'}), name='group-list-permssion')
]
