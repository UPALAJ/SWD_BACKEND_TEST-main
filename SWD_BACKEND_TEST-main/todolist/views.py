from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todolist.serializers import ToDoListSerializer
from todolist.models import todolistmodel

# Create your views here.
@api_view(['POST'])
def todolist_create(request):
    serializer = ToDoListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def todolist_update(request):
    try:
        item = todolistmodel.objects.get(pk=request.data.get('pk'))
    except todolistmodel.DoesNotExist:
        return Response({'error'}, status=400)
    
    serializer = ToDoListSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def todolist_delete(request):
    try:
        item = todolistmodel.objects.get(pk=request.data.get('pk'))
    except todolistmodel.DoesNotExist:
        return Response({'error'}, status=400)
    
    item.delete()
    return Response(status=204)