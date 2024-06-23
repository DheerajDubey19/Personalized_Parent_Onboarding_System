from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Parent
from parent.serializers import ParentSerializer

# ParentViewSet handles all CRUD operations for the Parent model
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    # Define a custom action for GET requests on a specific parent
    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        parent = self.get_object()
        return Response({"detail": f"GET request for parent {parent.id}"})

    # Define a custom action for POST requests on a specific parent
    @action(detail=False, methods=['post'])
    def custom_action_post(self, request):
        return Response({"detail": "POST request"})

    # Define a custom action for PUT requests on a specific parent for any update
    @action(detail=True, methods=['put'])
    def custom_action_put_patch(self, request, pk=None):
        parent = self.get_object()
        return Response({"detail": f"PUT request for parent {parent.id}"})

    # Define a custom action for DELETE requests for deleting a any specific parent details
    @action(detail=True, methods=['delete'])
    def custom_action_delete(self, request, pk=None):
        parent = self.get_object()
        parent.delete()
        return Response({"detail": f"Deleted parent {parent.id}"})