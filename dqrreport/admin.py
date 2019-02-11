from django.contrib import admin
from . models import obsinfo
from . models import dqrstats
from . models import dph
from . models import housekeeping

# Register your models here.
admin.site.register(obsinfo)
admin.site.register(dqrstats)
admin.site.register(dph)
admin.site.register(housekeeping)