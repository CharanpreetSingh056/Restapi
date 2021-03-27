from django.shortcuts import render,redirect

from django.http import JsonResponse

from rest_framework.decorators import api_view

from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.
@api_view(['GET'])
def temp(request):
    tasks= Task.objects.all()
    serializer=TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskspec(request,pk):
    tasks= Task.objects.get(id=pk)
    serializer=TaskSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def upload(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def update(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=tasks,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request,pk):
    tasks=Task.objects.get(id=pk)
    tasks.delete()

    return Response('Successfully deleted.')

