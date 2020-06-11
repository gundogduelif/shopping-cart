# shopping_cart.py

import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print("---------------------------------")
print("KINGS GOURMET FOODS GROCERY")
print("WEB: WWW.KINGSGOURMETFOODSGROCERY.COM")
print("ADDRESS: 1508 Kings Hwy, Brooklyn, NY 11229")
print("PHONE:(917) 222-3344")
print("---------------------------------")
now = datetime.datetime.now()
print("CHECK OUT AT:   " + now.strftime("%Y-%m-%d %H:%M")) # DateTime REFERENCE: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
  
product_total = 0
product_ids = [] #The Infinite Loop REFERENCE : https://www.tutorialspoint.com/python/python_while_loop.htm
var = 1               
while var == 1 : 
  product_id = input('Please input a product identifier:') 
  if product_id == "DONE":
        break  
  else: product_ids.append(product_id) 

print("SHOPPING CARD IDENTIFIERS INCLUDE:",(product_ids))
# Python List append() REFERENCE : https://www.youtube.com/watch?v=3BaGb-1cIr0&feature=youtu.be
#product_ids = [1, 8, 6, 16, 6]   
#print("SHOPPING CARD IDENTIFIERS INCLUDE:",(product_ids))

for product_id in product_ids:
  matching_products = [p for p in products if str(p["id"]) == str(product_id)]
  matching_product = matching_products[0]
  usd = "${0:.2f}".format(matching_product["price"])
  print(" + " + matching_product["name"] + " (" + str(usd) + ")")
  product_total = product_total + matching_product["price"]
  tax_total = (product_total * 8.75)/100 
  grand_total = product_total + tax_total

print("---------------------------------")
print("SUBTOTAL:" + str(round(product_total, 2)))
print("NY SALES TAX:" + str(round(tax_total, 2)))
print("TOTAL:" + str(round(grand_total, 2)))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")


# product_id_limit = [l for l in products if str(l["id"]) < str(product_id)]:

# def greater_than_twenty(i):
#       return i > 20
#       list(filter(greater_than_twenty,product_ids))
#       print( "hello")

# for x in product_ids:
# matching_products = [p for p in products if p["id"] == x]
# print("Hey, are you sure that product identifier" + str(product_ids) + "is correct? Please try again!") 
                
# product_ids = products["id"]


# no_matches = [x for x in products if x >= 21]
# print('Hey, are you sure that product identifier is correct? Please try again!',no_matches)

# product_id != .join(map(str,products["id"]): 

# TO DO LIST

##### 1 A grocery store name of your choice
##### 2 A grocery store phone number and/or website URL and/or address of choice
##### 3 The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
##### 4 The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
##### 5 The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
##### 6 The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
##### 7 The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
##### 8 A friendly message thanking the customer and/or encouraging the customer to shop again
