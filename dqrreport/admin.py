from django.contrib import admin
from . models import obsinfo
from . models import dqrstats
from . models import dph
from . models import housekeeping
from . models import countrate
from . models import datainteg
from . models import datasat
from . models import noisefrag

# Register your models here.
admin.site.register(obsinfo)
admin.site.register(dqrstats)
admin.site.register(dph)
admin.site.register(housekeeping)
admin.site.register(countrate)
admin.site.register(datainteg)
admin.site.register(datasat)
admin.site.register(noisefrag)