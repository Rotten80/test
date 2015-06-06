#encoding: UTF-8

from django.db import models

# Create your models here.

class CarModel(models.Model):

    nam = models.CharField(default="",max_length=100)

    def __unicode__(self):
        return self.nab

    class Meta:
        db_table = "car_model"
