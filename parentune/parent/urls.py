from django.urls import path, include
from rest_framework.routers import DefaultRouter
from parent.views import ParentViewSet

# Create a router and register the ParentViewSet with it
router = DefaultRouter()
router.register('', ParentViewSet)

urlpatterns = [
    # Include the URLs from the router (which includes the ParentViewSet URLs)
    path('', include(router.urls)),
]