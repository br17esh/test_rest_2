from django.db import models

class summary(models.Model):
    UID = models.IntegerField() 
    folder = models.CharField(max_length=50)
    # OBSID = models.CharField(max_length=50)
    Observer = models.CharField(max_length=50)
    # Object = models.CharField(max_length=50)
    # RA = models.FloatField()
    # Decr = models.FloatField()
    # Exposure_time = models.FloatField()
    # RA = models.DecimalField(max_digits=20, decimal_places=None)
    # Decr = models.DecimalField(max_digits=20, decimal_places=None)
    # Exposure_time = models.DecimalField(max_digits=20, decimal_places=None)
    # Date_time_start = models.DateTimeField()
    # Date_time_end = models.DateTimeField()

    def __str__(self):
        return self.folder