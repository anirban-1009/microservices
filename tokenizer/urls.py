from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tokenizer.views import TokensListViewSet

router = DefaultRouter()
router.register(r'list', TokensListViewSet, basename='token-list')

urlpatterns = [
    path('', include(router.urls)),
]