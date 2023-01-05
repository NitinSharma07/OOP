class Item:
    pay_rate = 0.8 #The pay rate after 20% discount      # This is the class attribute
    all = []
    def __init__(self,name:str, price:float, quantity=0) :
        
        assert price >= 0, f"Price {price} is not greater than or equal to zero, but lesss than zero."   #by assert we are providing the specifications or the conditions that should be applied to the method inputs

        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero, but lesss than zero."

        self.name = name        #These are the method attributes
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item ('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone",100, 1)
item2 = Item("Laptop",1000, 3)
item1 = Item("Cable",10, 5)
item1 = Item("Mouse",50, 5)
item1 = Item("Keyboard",75, 5)
item1.apply_discount()
print(item1.price)

print(Item.all)










