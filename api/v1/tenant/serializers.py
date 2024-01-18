from rest_framework import serializers
from tenant_management.models import Tenant, TenantAssignment


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.tenants.exists():
            unit_data = [
                {
                    "property_id": assignment.unit.property.id,
                    "property_name": assignment.unit.property.name,
                    "unit_id": assignment.unit.id,
                    "unit_type": assignment.unit.unit_type,
                }
                for assignment in instance.tenants.all()
            ]
            representation["unit_details"] = unit_data

        return representation


class TenantAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantAssignment
        fields = "__all__"
