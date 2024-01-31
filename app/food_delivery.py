class FoodDeliverySystem:
    """Objeto de gerenciamento dos pedidos."""
    order_id = 0
    orders_log = {}
    def __init__(self):
        self.menu = {
            "Burger": [15, "https://static3.depositphotos.com/1000691/109/i/380/depositphotos_1098427-stock-photo-cheeseburger.jpg"],
            "Pizza": [25, "https://st2.depositphotos.com/30394798/42225/i/380/depositphotos_422250918-stock-photo-italian-pizza-melted-mozzarella-cheese.jpg"],
            "Macarrão": [20, "https://static4.depositphotos.com/1006137/306/i/380/depositphotos_3061419-stock-photo-spaghetti-alla-bolognese.jpg"],
            "Salada": [12, "https://st2.depositphotos.com/2534661/6185/i/380/depositphotos_61856025-stock-photo-fresh-salad.jpg"],
            "Bebidas": [13, "https://static8.depositphotos.com/1020618/980/i/380/depositphotos_9805108-stock-photo-glass-of-cola.jpg"],
            "Miojo": [15, "https://st.depositphotos.com/1177973/4353/i/380/depositphotos_43532147-stock-photo-instant-noodles-isolated-on-white.jpg"],
            "Sushi": [27, "https://static9.depositphotos.com/1036708/1156/i/380/depositphotos_11564565-stock-photo-japanese-sushi.jpg"],
            "Pão": [35, "https://static8.depositphotos.com/1063437/871/i/380/depositphotos_8711334-stock-photo-loaf-of-bread-isolated-on.jpg"]
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
