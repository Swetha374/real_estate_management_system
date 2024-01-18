from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Unit
from .forms import PropertyForm, UnitForm


def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("property_list")
    else:
        form = PropertyForm()

    return render(request, "add_property.html", {"form": form})


def property_list(request):
    properties = Property.objects.all()
    return render(request, "property_list.html", {"properties": properties})


def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    units = property.units.all()
    return render(
        request, "property_detail.html", {"property": property, "units": units}
    )


def add_unit(request, property_id):
    property = Property.objects.get(pk=property_id)
    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.property = property
            unit.save()
            return redirect("property_detail", property_id=property_id)
    else:
        form = UnitForm()

    return render(request, "add_unit.html", {"form": form, "property": property})


def unit_list_view(request):
    units = Unit.objects.all()
    return render(request, "unit_list.html", {"units": units})
