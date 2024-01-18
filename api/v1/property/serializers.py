from rest_framework import serializers
from property_management.models import Property,Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Unit
        fields=("tenants","rent_cost","unit_type")

    def create(self, validated_data):
        validated_data["property_id"] = self.context.get("property_id")
        unit = super().create(validated_data)
        return unit

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model=Property
        fields="__all__"

    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.units.exists():  # Check if there are any units
            units_data = [
                {
                    "unit_type": unit.unit_type,
                    "rent_cost": unit.rent_cost,
                    "tenants": [
                        {
                            "tenant_name": tenant_assignment.tenant.name,
                            "agreement_end_date": tenant_assignment.agreement_end_date,
                            "monthly_rent_date": tenant_assignment.monthly_rent_date,
                        }
                        for tenant_assignment in unit.tenants.all()
                    ],
                }
                for unit in instance.units.all()
            ]
            data["units"] = units_data
        return data