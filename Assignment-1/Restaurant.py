class MenuItem:
    def __init__(self, name_of_dish, price_of_dish, category):
        self.name_of_dish = name_of_dish
        self.price_of_dish = price_of_dish
        self.category = category

class Order:
    def __init__(self, order_id, customer, list_of_items, menu_dict):
        self.order_id = order_id
        self.customer = customer
        self.list_of_items = list_of_items
        self.menu_dict = menu_dict
        self.total_price = self.calculate_total_price()  # Call method to calculate total price
    
    def calculate_total_price(self):
        total = 0
        for item_name in self.list_of_items:
            if item_name in self.menu_dict:
                total += self.menu_dict[item_name].price_of_dish
        return total

class Customer:
    def __init__(self, name, phoneno):
        self.name = name
        self.phoneno = phoneno
        self.list_of_orders = []

    def add_order(self, order):
        self.list_of_orders.append(order)

class Restaurant:
    def __init__(self):
        self.menu_dict = {}  # Dictionary to store MenuItem objects
        self.orders = []  # List to store Order objects

    def add_dish(self, name_of_dish, price_of_dish, category):
        new_dish = MenuItem(name_of_dish, price_of_dish, category)
        self.menu_dict[name_of_dish] = new_dish

    def remove_dish(self, name_of_dish):
        if name_of_dish in self.menu_dict:
            del self.menu_dict[name_of_dish]
        else:
            print(f"Dish '{name_of_dish}' not found in the menu.")

    def place_order(self, order_id, customer, list_of_dish_names):
        # List of item names directly
        list_of_items = list_of_dish_names
        new_order = Order(order_id, customer, list_of_items, self.menu_dict)
        customer.add_order(new_order)
        self.orders.append(new_order)
        return new_order

    def calculate_total_sales(self):
        return sum(order.total_price for order in self.orders)

    def display_menu(self):
        if not self.menu_dict:
            print("Menu is empty.")
        else:
            for dish in self.menu_dict.values():
                print(f"Dish: {dish.name_of_dish}, Price: {dish.price_of_dish}, Category: {dish.category}")

# Example usage
restaurant = Restaurant()
restaurant.add_dish("Pizza", 500, "Main Course")
restaurant.add_dish("Burger", 300, "Main Course")

customer1 = Customer("Bleh", "1234512345")

print("Menu:")
restaurant.display_menu()

order1 = restaurant.place_order(1, customer1, ["Pizza", "Burger"])
print(f"\nOrder ID: {order1.order_id}, Total Price: {order1.total_price}")

print(f"\nTotal Sales: {restaurant.calculate_total_sales()}")
