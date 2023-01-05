import csv
from item import Item
class Phone(Item):       # for inheritance inheriting methods of item in phone
    
    def __init__(self, name: str, price: float, quantity=0, broken_phones = 0):
        super().__init__(
            name, price , quantity
        )
        assert price >= 0, f"Price {price} is not greater than or equal to zero, but lesss than zero."  # by assert we are providing the specifications or the conditions that should be applied to the method inputs

        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero, but lesss than zero."
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero, but lesss than zero."

        self.name = name  # These are the method attributes
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones
