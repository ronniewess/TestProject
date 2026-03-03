from rest_framework import serializers
from .models import Task

# Serializer for Task model
# Used to translate data from API call
# ModelSerializer is a shortcut that automatically creates a serializer based on the model
# Meta class is used to specify the model and fields to include in the serializer (Django REST Framework documentation)
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']

def validate_status(value):
    valid_statuses = ['pending', 'in_progress', 'completed']
    if value not in valid_statuses:
        raise serializers.ValidationError(f"Status must be one of: {', '.join(valid_statuses)}")
    return value