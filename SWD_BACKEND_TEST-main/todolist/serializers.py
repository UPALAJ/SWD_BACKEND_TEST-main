from rest_framework import serializers
from .models import todolistmodel

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = todolistmodel
        fields = ['id', 'created_date', 'updated_date', 'element']