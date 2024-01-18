from django.contrib import admin
from tenant_management.models import (
  Tenant,
  TenantAssignment
)
admin.site.register(Tenant)
admin.site.register(TenantAssignment)



