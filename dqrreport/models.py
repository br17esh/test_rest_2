from django.db import models

# Create your models here.
class obsinfo(models.Model):
    UID = models.IntegerField() 
    date_obs = models.CharField(max_length=50)
    time_obs = models.CharField(max_length=50)
    date_end = models.CharField(max_length=50)
    time_end = models.CharField(max_length=50)
    obs_id = models.CharField(max_length=50)
    exposure = models.CharField(max_length=50)
    sourceid = models.CharField(max_length=50)
    observer = models.CharField(max_length=50)
    ra_pnt = models.CharField(max_length=50)
    dec_pnt = models.CharField(max_length=50)

    def __str__(self):
        return self.date_obs

class dqrstats(models.Model):
    UID = models.IntegerField()
    filename_OF = models.CharField(max_length=50)
    filename_FF = models.CharField(max_length=50)
    size_bytes_OF = models.CharField(max_length=50)
    size_bytes_FF = models.CharField(max_length=50)
    size_OF = models.CharField(max_length=50)
    size_FF = models.CharField(max_length=50)
    events_quadA_OF = models.CharField(max_length=50)
    events_quadA_FF = models.CharField(max_length=50)
    events_quadB_OF = models.CharField(max_length=50)
    events_quadB_FF = models.CharField(max_length=50)    
    events_quadC_OF = models.CharField(max_length=50)
    events_quadC_FF = models.CharField(max_length=50)
    events_quadD_OF = models.CharField(max_length=50)
    events_quadD_FF = models.CharField(max_length=50)
     
    def __str__(self):
        return self.filename_OF

class dph(models.Model):
    UID = models.IntegerField()
    quadA = models.CharField(max_length=200)
    quadB = models.CharField(max_length=200)
    quadC = models.CharField(max_length=200)
    quadD = models.CharField(max_length=200)
     
    def __str__(self):
        return self.quadA

class housekeeping(models.Model):
    UID = models.IntegerField()
    plot1 = models.CharField(max_length=200)
    plot2 = models.CharField(max_length=200)
    plot3 = models.CharField(max_length=200)
    plot4 = models.CharField(max_length=200)
    plot5 = models.CharField(max_length=200)
    plot6 = models.CharField(max_length=200)
    plot7 = models.CharField(max_length=200)
    plot8 = models.CharField(max_length=200)
    plot9 = models.CharField(max_length=200)
    plot10 = models.CharField(max_length=200)
    plot11 = models.CharField(max_length=200)
    plot12 = models.CharField(max_length=200)
    plot13 = models.CharField(max_length=200)
    plot14 = models.CharField(max_length=200)
    
    def __str__(self):
        return self.plot1        
