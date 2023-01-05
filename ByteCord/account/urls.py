from django.urls import path, include
from .api import RegisterApi
from .api import SimpleApi

urlpatterns = [
    path("api/register", RegisterApi.as_view()),
    path("api/hello", SimpleApi.as_view()),
]