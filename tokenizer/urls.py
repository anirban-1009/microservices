from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tokenizer.views import TokensListViewSet, TokensDetailViewSet

router = DefaultRouter()
router.register('list', TokensListViewSet, basename='token-list')
router.register(r'detail', TokensDetailViewSet, basename='token-detail')

urlpatterns = [
    path('', include(router.urls)),
]