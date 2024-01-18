from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_property, name='add_property'),
    path("list/", property_list, name="property_list"),
    path("<int:property_id>/", property_detail, name="property_detail"),
     path('add_unit/<int:property_id>/', add_unit, name='add_unit'),
    path('unit_list/', unit_list_view, name='unit_list'),
    path('detail/<int:property_id>/', property_detail, name='property_detail'),
]
