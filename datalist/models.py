from django.db import models
from django.utils import timezone


class CloudData(models.Model):
    location = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(
            default=timezone.now)
    bin_id = models.IntegerField()
    gw_id = models.IntegerField()
    

    def __str__(self):
        return self.location
