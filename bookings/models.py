from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):
    pass


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "duration": self.duration,
        }


class Reservation(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, blank=True)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)
    reference = models.CharField(max_length=4)
    email = models.EmailField()

    def __str__(self):
        return f"{self.customer.email} for {self.service.name} at {self.datetime}"


class Day(models.Model):
    date = models.DateField()
    one = models.ForeignKey(
        "Reservation",
        on_delete=models.CASCADE,
        blank=True,
        related_name="one",
        null=True,
    )
    two = models.ForeignKey(
        "Reservation",
        on_delete=models.CASCADE,
        blank=True,
        related_name="two",
        null=True,
    )
    three = models.ForeignKey(
        "Reservation",
        on_delete=models.CASCADE,
        blank=True,
        related_name="three",
        null=True,
    )
    four = models.ForeignKey(
        "Reservation",
        on_delete=models.CASCADE,
        blank=True,
        related_name="four",
        null=True,
    )
    five = models.ForeignKey(
        "Reservation",
        on_delete=models.CASCADE,
        blank=True,
        related_name="five",
        null=True,
    )
    six = models.ForeignKey(
        "Reservation",
        on_delete=models.CASCADE,
        blank=True,
        related_name="six",
        null=True,
    )
    seven = models.ForeignKey(
        "Reservation",
        on_delete=models.CASCADE,
        blank=True,
        related_name="seven",
        null=True,
    )
    eight = models.ForeignKey(
        "Reservation",
        on_delete=models.CASCADE,
        blank=True,
        related_name="eight",
        null=True,
    )
