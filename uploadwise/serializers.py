from rest_framework import serializers
from . models import upobsid

class upobsidSerializer(serializers.ModelSerializer):

    class Meta:
        model = upobsid
        #fields = ('firstname','lastname')
        fields = '__all__'
