from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import dqrstats
from . serializers import dqrstatsSerializer
from . models import dph
from . serializers import dphSerializer
from . models import obsinfo
from . serializers import obsinfoSerializer
from . models import housekeeping
from . serializers import housekeepingSerializer
from . models import countrate
from . serializers import countrateSerializer

# Create your views here.
class obsinfoList(APIView):

    def get(self, request):
        obsinfo1 = obsinfo.objects.all()
        serializer = obsinfoSerializer(obsinfo1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class dqrstatsList(APIView):

    def get(self, request):
        dqr1 = dqrstats.objects.all()
        serializer = dqrstatsSerializer(dqr1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class dphList(APIView):

    def get(self, request):
        dph1 = dph.objects.all()
        serializer = dphSerializer(dph1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class countrateList(APIView):

    def get(self, request):
        ctrate = countrate.objects.all()
        serializer = countrateSerializer(ctrate,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class housekeepingList(APIView):

    def get(self, request):
        house1 = housekeeping.objects.all()
        serializer = housekeepingSerializer(house1,many=True)
        return Response(serializer.data)

    def post(self):
        pass