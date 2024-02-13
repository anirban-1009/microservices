from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_mgmt.views import UsersDetailViewSet, UsersListViewSet, LoginAPIView, LogOutAPIView

router = DefaultRouter()
router.register('', UsersListViewSet, basename='user-list')
router.register(r'detail', UsersDetailViewSet, basename='user-detail')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogOutAPIView.as_view())
]
