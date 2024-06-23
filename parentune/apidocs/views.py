from django.urls import path
from .views import swagger_ui_view

urlpatterns = [
    path('api-docs/', swagger_ui_view, name='swagger-ui'),  # Endpoint for Swagger UI
]
