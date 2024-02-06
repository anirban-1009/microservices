from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_mgmt.views import UsersDetailViewSet, UsersListViewSet

router = DefaultRouter()
router.register('list', UsersListViewSet, basename='user-list')
router.register(r'list', UsersDetailViewSet, basename='user-detail')

urlpatterns = [
    path('', include(router.urls)),
]
