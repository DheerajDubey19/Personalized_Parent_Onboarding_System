"""
URL configuration for parentune project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

# Define schema view for OpenAPI schema
openapi_schema_view = get_schema_view(
    title="Parentune Assessment API",
    description="API for interacting with Parentune project",
    version="1.0.0",
    public=True,  # Set to False to restrict access
)


# URL patterns for the project, directing to different apps
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('api/v1/parent/', include('parent.urls')),  # Parent app API endpoints
    path('api/v1/child/', include('child.urls')),  # Child app API endpoints
    path('api/v1/content/', include('content.urls')),  # Content app API endpoints
    path('api/v1/swagger-ui/', TemplateView.as_view(template_name='swagger_ui.html',extra_context={'schema_url': 'openapi-schema'}), name='swagger-ui'),
    path('openapi-schema/', openapi_schema_view, name='openapi-schema'),
]
