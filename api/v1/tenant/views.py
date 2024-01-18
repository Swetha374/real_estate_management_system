from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from tenant_management.models import Tenant, TenantAssignment
from .serializers import TenantSerializer, TenantAssignmentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class TenantListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class TenantDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class TenantAssignmentListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = TenantAssignment.objects.all()
    serializer_class = TenantAssignmentSerializer
