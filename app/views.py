from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from .food_delivery import FoodDeliverySystem

def display_menu(request):
    food_system = FoodDeliverySystem()
    menu_details = food_system.display_menu()
    return render(request, 'index.html', {'menu_details': menu_details})

def place_order(request, customer_name, order_items):
    food_system = FoodDeliverySystem()
    order_details = food_system.place_order(customer_name, order_items)
    return JsonResponse(order_details)
