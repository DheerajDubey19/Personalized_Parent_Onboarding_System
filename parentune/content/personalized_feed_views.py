from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from parent.models import Parent
from child.models import Child
from content.models import Content
from content.serializers import ContentSerializer
from django.db.models import Q
import random

class PersonalizedHomeFeedView(APIView):
    def get(self, request, parent_id):
        try:
            # Fetch the parent object based on the provided parent_id
            parent = Parent.objects.get(id=parent_id)
            
            # Fetch all child objects associated with the parent
            children = Child.objects.filter(parent=parent)

            # Check if age filter parameter is provided in request
            age_filter_param = request.query_params.get('age', None)
            
            # Check if gender filter parameter is provided in request
            gender_filter_param = request.query_params.get('gender', None)
            
            # Check if parent_type filter parameter is provided in request
            parent_type_filter_param = request.query_params.get('parent_type', None)

            # Initialize all_content to an empty dictionary
            all_content = {}

            # If any filter parameter is provided, apply the filters
            if age_filter_param or gender_filter_param or parent_type_filter_param:
                query = Q()
                if age_filter_param:
                    query &= (Q(min_age__lte=age_filter_param) & Q(max_age__gte=age_filter_param))
                if gender_filter_param:
                    query &= Q(gender=gender_filter_param)
                if parent_type_filter_param:
                    query &= Q(parent_type=parent_type_filter_param)
                
                # Fetch the filtered content, limited to the 5 most recently updated
                all_content = Content.objects.filter(query).distinct().order_by("-updatedOn")[:5]

            # If no children, fetch 5 random blog posts
            elif not children.exists():
                all_content = Content.objects.all().order_by("-updatedOn")[:5]

            # If parent has children, fetch content based on children's age and gender
            elif children.exists():
                query = Q()
                for child in children:
                    query |= Q(min_age__lte=child.age, max_age__gte=child.age, gender=child.gender)
                
                # Fetch the filtered content, limited to the 5 most recently updated
                all_content = Content.objects.filter(query).distinct().order_by("-updatedOn")[:5]

            # Serialize all_content, allowing for multiple entries
            serializer = ContentSerializer(all_content, many=True)
            
            # Return the serialized data as a response
            return Response(serializer.data)

        except Parent.DoesNotExist:
            return Response({"error": "Parent does not exist."}, status=status.HTTP_404_NOT_FOUND)
