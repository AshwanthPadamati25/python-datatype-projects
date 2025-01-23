class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
        self.you_saved=price-deal_price
         
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("Rating: {}".format(self.ratings))
        print("You Save: {}".format(self.you_saved))
        
    def get_deal_price(self):
        return self.deal_price
    
class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months
        
    def display_product_details(self):
        super().display_product_details()
        print("Warranty: {} months".format(self.warranty_in_months))
    
class GroceryItem(Product):
    def __init__(self, name, price, deal_price, you_save, expiry_date):
        super().__init__(name, price, deal_price, you_save)
        self.expiry_date=expiry_date
        
    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date: {}".format(self.expiry_date))
        
class laptop(Product):
    def __init__(self, name, price, deal_price, ratings, ram, storage):
        super().__init__(name, price, deal_price, ratings)
        self.ram=ram
        self.storage=storage
    
    def display_product_details(self):
        super().display_product_details()
        print("Ram: {}".format(self.ram))
        print("Storage: {}".format(self.storage))    
        
class Order:
    delivery_charges = {
        "Normal":0,
        "Prime Delivery":100,
    }
    def __init__(self, delivery_method, delivery_adress):
        self.items_in_cart=[]
        self.delivery_method=delivery_method
        self.delivery_adress=delivery_adress
    
    def add_items(self, product, quantity):
        item = (product, quantity)
        self.items_in_cart.append(item)
        
    def display_order_details(self):
        print("Delivery Method: {}".format(self.delivery_method))
        print("Delivery Charges: {}".format(self.delivery_charges))
        print("Products")
        print("----------------------------")
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quaantity: {}".format(quantity))
            print("")
        print("----------------------------")
        total_bill = self.get_total_bill()
        print("Total Bill {}".format(total_bill))
            
    def get_total_bill(self):
        total_bill=0
        for product, quantity in self.items_in_cart:
            total_bill+=product.get_deal_price() * quantity
            
        order_delivery_charges = Order.delivery_charges[self.delivery_method]
        total_bill+=order_delivery_charges
        return total_bill
    
    @classmethod
    def update_delivery_charges(cls, delivery_method, charges):
        cls.delivery_charges[delivery_method]=charges
    
    
tv = ElectronicItem("TV", 25000, 15000, 4.5, 24)   
milk = GroceryItem("Milk", 35, 30, 5, 2024)

my_order=Order("Normal", "Hyderabad")
my_order.add_items(tv, 1)
my_order.add_items(milk, 3)
Order.update_delivery_charges("Normal", 10)

lenovo_lap=laptop("Lenovo 123", 45000, 30000, 4.5, 24, "16 GB")
lenovo_lap.display_product_details()