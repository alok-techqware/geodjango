from django.db import models
from django.contrib.gis.db import models # GeoDjango Model API
from django.utils.translation import gettext_lazy as _


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.PointField(null=True) # Spatial Field Types

    def __str__(self) -> str:
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()

    def __str__(self):
        return self.name

class HotelTwoT(models.Model):
    name = models.CharField(max_length=255)
    street_1 = models.CharField(max_length=200)
    street_2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    location = models.PointField(null=True)  # Spatial Field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("HotelTwoT")
        verbose_name_plural = _("HotelTwoTs")

    def __str__(self):
        return f"{self.street_1}, {self.city}, {self.state}, {self.country}"
    
class points(models.Model):
    name=models.CharField(max_length=20)
    location = models.PointField()
    description=models.CharField(max_length=200,blank=True)