from rest_framework import serializers
from . models import dqrstats
from . models import dph
from . models import obsinfo
from . models import housekeeping
from . models import countrate
from . models import datainteg
from . models import datasat
from . models import noisefrag

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

class countrateSerializer(serializers.ModelSerializer):

    class Meta:
        model = countrate
        fields = '__all__'

class housekeepingSerializer(serializers.ModelSerializer):

    class Meta:
        model = housekeeping
        fields = '__all__'

class dataintegSerializer(serializers.ModelSerializer):

    class Meta:
        model = datainteg
        fields = '__all__'

class datasatSerializer(serializers.ModelSerializer):

    class Meta:
        model = datasat
        fields = '__all__'

class noisefragSerializer(serializers.ModelSerializer):

    class Meta:
        model = noisefrag
        fields = '__all__'
