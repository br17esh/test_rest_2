from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import upobsid
from . serializers import upobsidSerializer

# Create your views here.
class upobsidList(APIView):

    def get(self, request):
        up1 = upobsid.objects.all()
        serializer = upobsidSerializer(up1,many=True)
        return Response(serializer.data)


    def post(self):
        pass