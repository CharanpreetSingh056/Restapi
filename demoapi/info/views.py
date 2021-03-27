from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import data
from .serializers import dataSerializer


# Create your views here.

class alldata(APIView):

    def get(self,request):
        data1 = data.objects.all()
        serializer= dataSerializer(data1, many=True)
        return Response(serializer.data)
        

    def post(self):
        pass

