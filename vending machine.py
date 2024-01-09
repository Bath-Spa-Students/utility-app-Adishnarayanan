A1 ={"Item": "Mountain Dew", "Price": "3.00", "Stock":"12"}
A2 ={"Item": "Pepsi", "Price": "3.00", "Stock":"15"}
B1= {"Item": "Oman chips", "Price": "1.00", "Stock":"10"}
B2= {"Item": "Sohar chips", "Price": "1.00", "Stock":"8"}
C1= {"Item": "kikat", "Price": "4.00", "Stock":"10"}
C2= {"Item": "Snickers", "Price": "5.00", "Stock":"5"}
D1= {"Item": "Water", "Price": "1.00", "Stock":"20"}
D2= {"Item": "Juice", "Price": "2.00", "Stock":"10"}
E1= {"Item": "Red Bull", "Price": "10.00", "Stock":"10"}
E2= {"Item": "Monster", "Price": "15.00", "Stock":"10"}

print("-----------------------------------------------------------------")
 
print("""HELLO!

WELCOME TO ADISH'S VENDING MACHINE 

WE HAVE VARIOUS VARIETIES OF SNACKS , CHOCOLATE  
AND DRINKS FOR YOU""") 
print("""+----------------------------------------------------------------------------+
|                            ADISH'S VENDING MACHINE                         |
|                                                                            |
|                                    MENU                                    |
+----------------------------------------------------------------------------+
|                                 DRINKS &SNACKS                             |
+----------------------------------------------------------------------------+
|Code|            ITEMS                 |       PRICE       |  ON THE MARKET |
+----------------------------------------------------------------------------+
| 01 | MOUNTAIN DEW                     |       3.00        |       12       | 
| 02 | PEPSI                            |       3.00        |       15       |
| 03 | OMAN CHIPS                       |       1.50        |       10       |
| 04 | SOHAR CHIPS                      |       1.50        |       08       |
| 05 | KIKAT                            |       4.00        |       10       |  
+----------------------------------------------------------------------------+
|                              DRINKS & CHOCOLATE                            |
+----------------------------------------------------------------------------+
|Code|              ITEMS               |      PRICE      |  ON THE MARKET   |
+----------------------------------------------------------------------------+
| 06 | SNICKERS                         |      5.00       |       05         |
| 07 | WATER                            |      1.00       |       20         |
| 08 | JUICE                            |      2.00       |       10         |
| 09 | REDBULL                          |     10.00       |       10         |
| 10 | MONSTER                          |     15.00       |       10         | 
+----------------------------------------------------------------------------+""")
items = (A1,A2,B1,B2,C1,C2,D1,D2,E1,E2)

print("Items Available for Purchase:")


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
