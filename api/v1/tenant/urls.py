from django.urls import path
from .views import *


urlpatterns = [
    path("list-create/", TenantListCreateView.as_view()),
    path("<int:pk>/", TenantDetailView.as_view()),
    path("assignment/list-create/", TenantAssignmentListCreateView.as_view()),

  


   
]
