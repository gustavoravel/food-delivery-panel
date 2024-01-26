class FoodDeliverySystem:
    order_id = 0
    orders_log = {}
    def __init__(self):
        self.menu = {
            "Burger": 15,
            "Pizza": 25,
            "Macarrão": 20,
            "Salada": 12,
            "Bebidas": 13,
            "Miojo": 15,
            "Sushi": 27,
            "Pão": 35
            # Add more items to the menu
        }
        self.bill_amount = 0
        
    def display_menu(self):
        
        menu_details = {item: price for item, price in self.menu.items()}
        
        return menu_details

        
    def place_order(self, customer_name, order_items):

        order_id = FoodDeliverySystem.order_id
        order_details = {
            "customer_name": customer_name,
            "order_items": order_items,
            "status": "Placed"
        }

        FoodDeliverySystem.orders_log[order_id] = order_details
        FoodDeliverySystem.order_id += 1
        return FoodDeliverySystem.orders_log
        
    def pickup_order(self, order_id):

        order_details = FoodDeliverySystem.orders_log.get(order_id)

        if order_details and order_details["status"] == "Placed":
            order_details["status"] = "Picked Up"
            return {order_id: order_details}
        else:
            return None
        
    def deliver_order(self, order_id):

        order_details = FoodDeliverySystem.orders_log.get(order_id)

        if order_details and order_details["status"] == "Picked Up":
            order_details["status"] = "Delivered"
            return f"Order {order_id} delivered successfully."
        return None

        
    def modify_order(self, order_id, new_items):

        order_details = FoodDeliverySystem.orders_log.get(order_id)

        if order_details and order_details["status"] == "Placed":
            available_items = {item: quantity for item, quantity in new_items.items() if item in self.menu}
            order_details["order_items"].update(available_items)
            return {order_id: order_details}
        else:
            return None
    
    def generate_bill(self, order_id):

        order_details = FoodDeliverySystem.orders_log.get(order_id)

        if order_details:
            items = order_details["order_items"]
            for item, quantity in items.items():
                self.bill_amount += self.menu[item] * int(quantity)

            if self.bill_amount > 100:
                total_bill_amount = self.bill_amount + (0.1 * self.bill_amount)
            else:
                total_bill_amount = self.bill_amount + (0.05 * self.bill_amount)

            return total_bill_amount
        else:
            return None
        
    def cancel_order(self, order_id):

        order_details = FoodDeliverySystem.orders_log.get(order_id)

        if order_details and order_details["status"] == "Placed":
            del FoodDeliverySystem.orders_log[order_id]
            return f"Order {order_id} canceled successfully."
        else:
            return None
