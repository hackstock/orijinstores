from django.urls import path
from .views import (
    StoriesApiView,
)

urlpatterns = [
    path('api', StoriesApiView.as_view()),
]