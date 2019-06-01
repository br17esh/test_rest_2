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
from . models import datainteg
from . serializers import dataintegSerializer
from . models import datasat
from . serializers import datasatSerializer
from . models import noisefrag
from . serializers import noisefragSerializer
# from . models import pixelprop
# from . serializers import pixelpropSerializer
# from . models import quadprop
# from . serializers import quadpropSerializer

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

class dataintegList(APIView):

    def get(self, request):
        dinteg1 = datainteg.objects.all()
        serializer = dataintegSerializer(dinteg1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class datasatList(APIView):

    def get(self, request):
        datasat1 = datasat.objects.all()
        serializer = datasatSerializer(datasat1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class noisefragList(APIView):

    def get(self, request):
        noise1 = noisefrag.objects.all()
        serializer = noisefragSerializer(noise1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

# class pixelpropList(APIView):
#
#     def get(self, request):
#         pprop1 = pixelprop.objects.all()
#         serializer = pixelpropSerializer(pprop1,many=True)
#         return Response(serializer.data)
#
#     def post(self):
#         pass

# class quadpropList(APIView):
#
#     def get(self, request):
#         qprop1 = topno.objects.all()
#         serializer = quadpropSerializer(qprop1,many=True)
#         return Response(serializer.data)
#
#     def post(self):
#         pass

