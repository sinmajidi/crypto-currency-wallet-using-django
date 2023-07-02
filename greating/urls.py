
from django.urls import path,include
from .views import Index,About

urlpatterns = [
    path('', Index.as_view(),name='index'),
    path('about/', About.as_view(),name='about'),
]
