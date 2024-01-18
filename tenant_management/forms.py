from django import forms
from .models import TenantAssignment,Tenant


class TenantAssignmentForm(forms.ModelForm):
    class Meta:
        model = TenantAssignment
        fields = ["tenant", "unit", "agreement_end_date", "monthly_rent_date"]


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ["name", "address", "document_proofs"]
