class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price
        
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("You Saved: {}".format(self.you_save))
        print("Rating: {}".format(self.ratings))
        
    def get_deal_price(self):
        return self.deal_price
    
class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, rating, warranty_in_months):
        super().__init__(name,price, deal_price, rating)
        self.warranty_in_months = warranty_in_months
    
    def display_product_details(self):
        super().display_product_details()
        print("Warranty in months: {}".format(self.warranty_in_months))
        print()
        
class GroceryItem(Product):
    def __init__(self, name, price, deal_price, rating, expiry_date):
        super().__init__(name,price,deal_price,rating)
        self.expiry_date = expiry_date
    
    def display_grocery_item_details(self):
        super().display_product_details()
        print("Expiry Date: {}".format(self.expiry_date))
        
class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address
        
    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))
        
    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
    
    def get_total_bill(self):
        total_bill=0
        for product, quantity in self.items_in_cart:
            price=product.get_deal_price() * quantity
            total_bill += price
        print("Total Bill: {}".format(total_bill))
        return total_bill

        
tv = ElectronicItem("TV", 30000, 25000, 4, 3)
tv.display_product_details()

milk = GroceryItem("Milk", 35, 30, 4, 2024)
milk.display_product_details()

