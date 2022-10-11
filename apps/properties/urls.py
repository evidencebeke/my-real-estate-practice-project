from django.urls import path
from . import views


urlpatterns = [
    path("all/", views.ListAllPropertiesAPIView.as_view(), name="all-properties"),
    path(
        "agents/", views.ListAgentsPropertiesAPIView.as_view(), name="agents-properties"
    ),
    path("create/", views.create_property_api_view, name="property_create"),
    path(
        "details/<slug:slug>/",
        views.PropertyDetailAPIView.as_view(),
        name="property-details",
    ),
    path(
        "update/<slug:slug>/", views.update_properties_api_view, name="update-property"
    ),
    path("delete/<slug:slug>", views.delete_property_api_view, name="delete_property"),
    path("search/", views.PropertySearchAPIView.as_view(), name="search-property"),
]
