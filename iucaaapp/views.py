from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import summary
from . serializers import summarySerializer

# Create your views here.
class summaryList(APIView):

    def get(self, request):
        summ = summary.objects.all()
        serializer = summarySerializer(summ.all(),many=True, read_only=True)
        return Response(serializer.data)

    def post(self):
        pass