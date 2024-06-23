from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from child.models import Child
from child.serializers import ChildSerializer

# ChildViewSet handles all CRUD operations for the Child model
class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

    # Define a custom action for GET requests on a specific child
    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        child = self.get_object()
        return Response({"detail": f"GET request for child {child.id}"})

    # Define a custom action for POST requests on a specific child
    @action(detail=False, methods=['post'])
    def custom_action_post(self, request):
        return Response({"detail": "POST request"})

    # Define a custom action for PUT requests for any update in a specific Child details
    @action(detail=True, methods=['put'])
    def custom_action_put_patch(self, request, pk=None):
        child = self.get_object()
        return Response({"detail": f"PUT request for child {child.id}"})

    # Define a custom action for DELETE requests for deleting specific child object
    @action(detail=True, methods=['delete'])
    def custom_action_delete(self, request, pk=None):
        child = self.get_object()
        child.delete()
        return Response({"detail": f"Deleted child {child.id}"})