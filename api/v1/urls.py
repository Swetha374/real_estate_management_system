from django.urls import path, include


urlpatterns = [
    path("admin/", include("api.v1.admin.urls")),
    path("property/", include("api.v1.property.urls")),
    path("tenant/", include("api.v1.tenant.urls")),

]
