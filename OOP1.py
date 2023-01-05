import csv
class Item:
    pay_rate = 0.8  # The pay rate after 20% discount      # This is the class attribute
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero, but lesss than zero."  # by assert we are providing the specifications or the conditions that should be applied to the method inputs

        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero, but lesss than zero."

        self.name = name  # These are the method attributes
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod         #This is used to convert the following method into the class and after converting it into the class, "self" will be replaced with the "cls"
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity')),
            )
    
    @staticmethod      
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e.: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"



# print(Item.all)  # without using __repr__ it is going to return  [Item, Item, Item, Item, Item] <- This list.
# Item.instantiate_from_csv()
# print(Item.all)    # here it is by reading through the files

# print(Item.is_integer(7))
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

phone1 = Phone("jscPhonev10", 500, 5, 1)
print(Item.all)
print(Phone.all)



