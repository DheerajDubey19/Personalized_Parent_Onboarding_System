from django.urls import path, include
from rest_framework.routers import DefaultRouter
from child.views import ChildViewSet

# Create a router and register the ChildViewSet with it
router = DefaultRouter()
router.register('', ChildViewSet)

urlpatterns = [
    # Include the URLs from the router (which includes the ChildViewSet URLs)
    path('', include(router.urls)),
]