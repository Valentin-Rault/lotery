from django.urls import path
from django.views.generic.base import TemplateView

from .views import showRandomPrize

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('getPrize', showRandomPrize, name='prize'),
]