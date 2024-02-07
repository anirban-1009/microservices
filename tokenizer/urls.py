from django.urls import include, path
from tokenizer.views import AuthView

urlpatterns = [
    path('', AuthView.as_view()),
]