from rest_framework import serializers
from . models import dqrstats
from . models import dph
from . models import obsinfo
from . models import housekeeping

class obsinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = obsinfo
        fields = '__all__'

class dqrstatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = dqrstats
        fields = '__all__'

class dphSerializer(serializers.ModelSerializer):

    class Meta:
        model = dph
        fields = '__all__'

class housekeepingSerializer(serializers.ModelSerializer):

    class Meta:
        model = housekeeping
        fields = '__all__'