from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views import View

from .models import Order
from .food_delivery import FoodDeliverySystem

class DisplayMenuView(View):
    def get(self, request, *args, **kwargs):
        food_system = FoodDeliverySystem()
        menu_details = food_system.display_menu()
        return render(request, 'index.html', {'menu_details': menu_details})

class PlaceOrderView(View):
    def post(self, request, customer_name, order_items, *args, **kwargs):
        food_system = FoodDeliverySystem()
        order_details = food_system.place_order(customer_name, order_items)
        Order.objects.create(customer_name=customer_name, order_items=order_items)
        return JsonResponse(order_details)
    
class PickUpOrderView(View):
    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id)
        if order.status == 'Placed':
            order.status = 'Picked Up'
            order.save
            return JsonResponse({"success": f"Pedido {order_id} foi retirado com sucesso."})
        else:
            return JsonResponse({"error": f"Pedido {order_id} ainda não foi lançado."}, status=400)
        
class DeliverOrderView(View):
    def post(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id)

        if order.status == 'Picked Up':
            order.status = 'Delivered'
            order.save()
            return JsonResponse({"success": f"Pedido {order_id} entregue com sucesso."})
        else:
            return JsonResponse({"error": f"Pedido {order_id} não foi retirado."}, status=400)
        
class ModifyOrderView(View):
    def post(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk = order_id)
        new_items = request.POST.get('new_items')

        if order.status == 'Placed':
            food_system = FoodDeliverySystem()
            available_items = {
                item: quantity for item, quantity in new_items.items() if item in food_system.menu
            }
            order.order_items.update(available_items)
            order.save()
            return JsonResponse({"success": f"Pedido {order_id} modificado com sucesso."})
        else:
            return JsonResponse({"error": f"Pedido {order_id} ainda não foi lançado."}, status=400)

class CancelOrderView(View):
    def post(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id)

        if order.status == 'Placed':
            order.delete()
            return JsonResponse({"success": f"Pedido {order_id} cancelado com sucesso."})
        else:
            return JsonResponse({"error": f"Pedido {order_id} não foi lançado."}, status=400)