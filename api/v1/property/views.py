from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from property_management.models import Property, Unit
from .serializers import PropertySerializer, UnitSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PropertiesListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertiesDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class UnitListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def get_queryset(self):
        return Unit.objects.filter(property_id=self.kwargs.get("property_id"))

    def get_serializer_context(self):
        return {
            "property_id": self.kwargs.get("property_id"),
        }
