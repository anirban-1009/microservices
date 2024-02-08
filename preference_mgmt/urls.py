from django.urls import include, path
from rest_framework.routers import DefaultRouter
from preference_mgmt.views import UpdateUserViewSet

router = DefaultRouter()
router.register('user-detail', UpdateUserViewSet, basename='user-detail')

urlpatterns = [
    path('', include(router.urls)),
]