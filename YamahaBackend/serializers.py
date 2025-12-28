from rest_framework import serializers
from .models import TestRide, Order

class TestRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestRide
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
