from django.urls import path
from .views import (
    assign_tenant,
    tenant_assignment_list,
    add_tenant,
    tenant_list,
    tenant_profile,
)

urlpatterns = [
    path("add/", add_tenant, name="add_tenant"),
    path("tenant_list/", tenant_list, name="tenant_list"),
    path("assign/", assign_tenant, name="assign_tenant"),
    path("assignment_list/", tenant_assignment_list, name="tenant_assignment_list"),
    path("<int:tenant_id>/profile/", tenant_profile, name="tenant_profile"),
]
