from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from content.models import Content
from content.serializers import ContentSerializer

# BlogViewSet handles all CRUD operations for the Content model
class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()    
    serializer_class = ContentSerializer

    # Define a custom action for GET requests on a specific blog
    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        blog = self.get_object()
        return Response({"detail": f"GET request for blog {blog.id}"})

    # Define a custom action for POST requests
    @action(detail=False, methods=['post'])
    def custom_action_post(self, request):
        return Response({"detail": "POST request"})

    # Define custom actions for PUT requests on a specific blog for any update
    @action(detail=True, methods=['put'])
    def custom_action_put_patch(self, request, pk=None):
        blog = self.get_object()
        return Response({"detail": f"PUT request for blog {blog.id}"})

    # Define a custom action for DELETE requests to delete a specific blog
    @action(detail=True, methods=['delete'])
    def custom_action_delete(self, request, pk=None):
        blog = self.get_object()
        blog.delete()
        return Response({"detail": f"Deleted blog {blog.id}"})
