from django.db import models

BEDROOM_CHOICES = (
    ("1BHK", "1BHK"),
    ("2BHK", "2BHK"),
    ("3BHK", "3BHK"),
    ("4BHK", "4BHK"),
)


class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.CharField(max_length=255)
    features = models.TextField()

    def __str__(self):
        return self.name


class Unit(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="units"
    )
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit_type = models.CharField(max_length=4, choices=BEDROOM_CHOICES)

    def __str__(self):
        return f"{self.property.name} - {self.unit_type}"
