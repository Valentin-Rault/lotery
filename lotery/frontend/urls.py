from django.urls import path
from django.views.generic.base import TemplateView

from .views import getRandomPrize

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('getPrize', getRandomPrize(), name='prize'),
]