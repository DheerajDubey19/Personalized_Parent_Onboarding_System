from rest_framework import serializers
from .models import Parent

# Serializer for the Parent model, includes all fields of the model
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'