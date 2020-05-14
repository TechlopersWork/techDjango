from django.urls import path
from . import views

urlpatterns = [
    path('techlopian/', views.techlopian),
    path('clients/', views.client),
]
