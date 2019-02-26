from django.db import models

class upobsid(models.Model):
    UID = models.IntegerField()
    OBSID = models.CharField(max_length=500)
    Datetime = models.CharField(max_length=50)

    r1 = models.CharField(max_length=500)
    r1size = models.CharField(max_length=50)
    r1date = models.CharField(max_length=50)

    r2 = models.CharField(max_length=500)
    r2size = models.CharField(max_length=50)
    r2date = models.CharField(max_length=50)

    r3 = models.CharField(max_length=500)
    r3size = models.CharField(max_length=50)
    r3date = models.CharField(max_length=50)



    def __str__(self):
        return self.OBSID