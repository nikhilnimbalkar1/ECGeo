from django.contrib.gis.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name},{self.address},{self.city}"
