class Cart:
    flat_discount=100
    min_bill=100
    def __init__(self):
        self.items={}
    def add_items(self,item_name,quantity):
        self.items[item_name]=quantity
        self.display_items()
    def display_items(self):
        print(self.items)
    
    @classmethod
    def update_flat_discount(cls, new_flat_discount):
        cls.flat_discount = new_flat_discount
        
    @staticmethod
    def greet():
        print("Have a great shopping")

print(Cart.flat_discount)
Cart.update_flat_discount(50)
print(Cart.flat_discount)
Cart.greet()