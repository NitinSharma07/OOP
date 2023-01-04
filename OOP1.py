class Item:
    pay_rate = 0.8 #The pay rate after 20% discount      # This is the class attribute
    def __init__(self,name:str, price:float, quantity=0) :
        
        assert price >= 0, f"Price {price} is not greater than or equal to zero, but lesss than zero."   #by assert we are providing the specifications or the conditions that should be applied to the method inputs

        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero, but lesss than zero."

        self.name = name        #These are the method attributes
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone",100, 1)
item2 = Item("Laptop",1000, 3)
item1 = Item("Cable",10, 5)
item1 = Item("Phone",50, 5)
item1 = Item("Phone",75, 5)
item1 = Item("Phone",100, 1)
item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7         #changed something out of the class named as Item
item2.apply_discount()
print(item2.price)

# print(item1.calculate_total_price())
# print(Item.__dict__)
# print(item2.__dict__)










