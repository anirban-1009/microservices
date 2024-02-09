from django.urls import include, path
from rest_framework.routers import DefaultRouter
from auth_mgmt.views import PermissionDetailViewSet, GroupDetailViewSet

router = DefaultRouter()
router.register('permission-detail', PermissionDetailViewSet, basename='permission-detail')
router.register('group-detail', GroupDetailViewSet, basename='group-detail')

urlpatterns = [
    path('', include(router.urls)),
    # Include the viewset itself for 'group-detail' endpoint
    path('groups/', GroupDetailViewSet.as_view({'get': 'list', 'post': 'create'}), name='group-list')
]
