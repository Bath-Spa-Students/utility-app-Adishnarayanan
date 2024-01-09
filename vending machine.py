from prettytable import prettytable
A1 ={"Item": "Dew", "Price": "3.00", "Stock":"12"}
A2 ={"Item": "Pepsi", "Price": "3.00", "Stock":"15"}
B1= {"Item": "Oman chips", "Price": "1.00", "Stock":"10"}
B2= {"Item": "Sohar chips", "Price": "1.00", "Stock":"8"}
C1= {"Item": "kikat", "Price": "4.00", "Stock":"10"}
C2= {"Item": "Snickers", "Price": "5.00", "Stock":"5"}
D1= {"Item": "Water", "Price": "1.00", "Stock":"20"}
D2= {"Item": "Juice", "Price": "2.00", "Stock":"10"}
E1= {"Item": "Red Bull", "Price": "10.00", "Stock":"10"}
E2= {"Item": "Monster", "Price": "15.00", "Stock":"10"}

items = (A1,A2,B1,B2,C1,C2,D1,D2,E1,E2)

table = prettytable()
table.field_names = ["Item", "Price", "Stock"]

for item in items:
    table.add_row([item["Item"], item["Price"], item["Stock"]])

print("Items Available for Purchase:")
print(table)

ITEMS = input("Enter the name of the item you want to buy: ")
item_code = None

for i in items:
    if ITEMS.lower() == i['Item'].lower():
        item_code = i
        break

if item_code is None:
    print("INVALID ITEM")
else:
    print(f"Awesome, {item_code['Item']} will cost you {item_code['Price']} $")

    price = float(input(f"Enter {item_code['Price']} dollars to purchase: "))
    if price == float(item_code['Price']):
        print(f"Thank you for your purchase. Here is your {item_code['Item']}.")
    else:
        print(f"Please enter only {item_code['Price']} dollars.")