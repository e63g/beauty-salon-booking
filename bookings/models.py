from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass


class Customer(models.Model):
    email = models.EmailField()
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, blank=True, related_name="cuser"
    )


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.PositiveIntegerField()


class Appointment(models.Model):
    customer = models.ForeignKey("User", on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    service = models.ManyToManyField(Service, related_name="service")
