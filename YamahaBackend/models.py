from django.db import models

class TestRide(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bikeModel = models.CharField(max_length=100)
    preferredDate = models.DateField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    part_name = models.CharField(max_length=200)
    price = models.CharField(max_length=20)

    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    payment_method = models.CharField(max_length=20)
    upi = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=30, blank=True, null=True)
    expiry = models.CharField(max_length=10, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.part_name
