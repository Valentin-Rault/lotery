from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('getPrize', TemplateView.as_view(template_name='prize.html'), name='prize'),
]