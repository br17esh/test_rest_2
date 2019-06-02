from rest_framework import serializers
from . models import summary

class summarySerializer(serializers.ModelSerializer):

    class Meta:
        model = summary
        #fields = ('firstname','lastname')
        fields = '__all__'
