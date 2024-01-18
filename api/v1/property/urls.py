from django.urls import path
from .views import *


urlpatterns = [
    path("list-create/", PropertiesListCreateView.as_view()),
    path("<int:pk>/", PropertiesDetailView.as_view()),
    path("<int:property_id>/units/list-create/", UnitListCreateView.as_view()),

  


   
]
