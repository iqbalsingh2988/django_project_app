from django.shortcuts import render
from rest_framework import viewsets

from my_awesome_api.serializers import PersonSerializer, SpeciesSerializer, TaskSerializer
from my_awesome_api.models import Person, Species, Task

from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
   queryset = Person.objects.all()
   serializer_class = PersonSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Species.objects.all()
   serializer_class = SpeciesSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response (serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response (serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response (serializer.data)