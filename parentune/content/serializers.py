from rest_framework import serializers
from content.models import Content

# Serializer for the Content model, includes all fields of the model
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'