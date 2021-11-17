from django.db import models
from django.utils.timezone import now

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=200)
    distance = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"the location is {self.location}"


# user = models.CharField(verbose_name="User",max_length=32)
# ip=models.IPAddressField(verbose_name="IP")
# lat= models.DecimalField(verbose_name="Lat",max_digits=10,decimal_places=1)
# long= models.DecimalField(verbose_name="Long",max_digits=10,decimal_places=1)
