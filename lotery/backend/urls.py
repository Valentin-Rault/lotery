from django.urls import path
from .views import RandomWord

urlpatterns = [
    path('random-word', RandomWord.as_view()),
]