from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TestRideSerializer, OrderSerializer
from .models import TestRide, Order

@api_view(['POST'])
def book_test_ride(request):
    serializer = TestRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Test ride booked"}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_test_rides(request):
    rides = TestRide.objects.all()
    serializer = TestRideSerializer(rides, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def place_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Order placed successfully!"}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
