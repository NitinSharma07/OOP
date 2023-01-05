import csv
from item import Item

item1 = Item('MyItem', 750)

# item1.name = "OtherItem"   #This can be achieved(will show error) if we use "item1._name", instead of "item1.name" 

# print(item1.__name) #it will show error reason is in item.py
item1.name = "OtherItem"
print(item1.name)




   








