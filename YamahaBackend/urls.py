from django.urls import path
from . import views

urlpatterns = [
    path('book-test-ride/', views.book_test_ride, name='book_test_ride'),
    path('get-test-rides/', views.get_test_rides, name='get_test_rides'),

    # Correct order URL
    path('create-order/', views.place_order, name='create_order'),
    path('get-orders/', views.get_orders, name='get_orders'),
]
