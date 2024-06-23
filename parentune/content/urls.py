from django.urls import path, include
from rest_framework.routers import DefaultRouter
from content.views import ContentViewSet
from content.personalized_feed_views import PersonalizedHomeFeedView

# Create a router and register the ContentViewSet with it
router = DefaultRouter()
router.register('', ContentViewSet)

# Define the urlpatterns, including the router's URLs and the custom view's URL
urlpatterns = [
    # Include the URLs from the router (which includes the ContentViewSet URLs)
    path('', include(router.urls)),
    
    # Add a custom URL pattern for the PersonalizedHomeFeedView
    path('personalized-feed/<int:parent_id>/', PersonalizedHomeFeedView.as_view(), name='personalized-feed'),
]
