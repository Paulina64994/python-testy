from django.db import models
from django.urls import reverse

# Create your models here.
class ListBike(models.Model):
    nameBike = models.CharField(max_length=255)
    content = models.TextField(default="")
    price = models.PositiveSmallIntegerField(default=1)
    year = models.PositiveSmallIntegerField(default=1800)
    imgBike = models.ImageField(upload_to='mediabike', blank=True, null=True)

    def __str__(self):
        return self.nameBike

    def is_expesive(self):
        return self.price > 1000

    def is_new(self):
        return self.year >2010

    def string_representation(self):
        return f"{self.nameBike} from {self.year}"

