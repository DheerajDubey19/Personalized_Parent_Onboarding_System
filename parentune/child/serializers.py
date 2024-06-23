from rest_framework import serializers
from child.models import Child

# Serializer for the Child model, includes all fields of the model
class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'