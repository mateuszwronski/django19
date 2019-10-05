from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('1', views.hello_world, name='hello_world'),
    path('2', views.HelloWorldView.as_view()),
    path('3', TemplateView.as_view(
        template_name='posts/index.html', extra_context=dict(name='Piotr'))),
]
