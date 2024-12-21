from django.db import models

# Create your models here.
# automation/models.py
from django.db import models

class Greenhouse(models.Model):
    name = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    light = models.FloatField()
    soil_moisture = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
