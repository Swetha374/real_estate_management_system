from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    document_proofs = models.FileField(upload_to="tenant_documents/")

    def __str__(self):
        return self.name


class TenantAssignment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="tenants")
    unit = models.ForeignKey(
        "property_management.Unit", on_delete=models.CASCADE, related_name="tenants"
    )
    agreement_end_date = models.DateField()
    monthly_rent_date = models.IntegerField()

    def __str__(self):
        return f"{self.tenant.name} - {self.unit.property.name}"
