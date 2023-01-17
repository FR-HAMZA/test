from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Cities'


class DeliveryMan(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Deliverymen'



class Package(models.Model):
    title = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'packages'


