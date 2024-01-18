from django.shortcuts import render, redirect, get_object_or_404
from .forms import TenantAssignmentForm, TenantForm
from .models import TenantAssignment, Tenant


def assign_tenant(request):
    if request.method == "POST":
        form = TenantAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tenant_assignment_list")
    else:
        form = TenantAssignmentForm()

    return render(request, "assign_tenant.html", {"form": form})


def tenant_assignment_list(request):
    tenant_assignments = TenantAssignment.objects.all()
    return render(
        request,
        "tenant_assignment_list.html",
        {"tenant_assignments": tenant_assignments},
    )


def add_tenant(request):
    if request.method == "POST":
        form = TenantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("tenant_list")
    else:
        form = TenantForm()

    return render(request, "add_tenant.html", {"form": form})


def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, "tenant_list.html", {"tenants": tenants})


def tenant_profile(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    assignments = TenantAssignment.objects.filter(tenant=tenant)

    return render(
        request, "tenant_profile.html", {"tenant": tenant, "assignments": assignments}
    )
