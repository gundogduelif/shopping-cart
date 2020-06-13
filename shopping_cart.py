# shopping_cart.py

import datetime
import string
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
 

valid_ids = range (1, 21, 1)           # range approach REFERENCE https://www.pythoncentral.io/pythons-range-function-explained/#:~:text=range()%20(and%20Python%20in,%2C%20but%20not%20including%2C%20stop%20.            
product_ids = []  #The Infinite Loop REFERENCE : https://www.tutorialspoint.com/python/python_while_loop.htm
var = 1                
while var == 1 : 
  product_id = input('Please input a product identifier:')
  if product_id == "DONE":
    break
  elif product_id == "done": 
    break
  elif product_id.isalpha():               # isalpha approach REFERENCE: https://www.w3schools.com/python/ref_string_isalpha.asp
      print ("Error Message Bar: Entered letters! Please input numbers only!")
  elif product_id in string.punctuation:   # string.punctuation https://www.geeksforgeeks.org/string-punctuation-in-python/
      print("Error Message Bar: Entered punctuation mark! Please input numbers only!") #Error Message bar: Please input numbers only!   
  elif int(product_id) in valid_ids:
        product_ids.append(product_id)
  else:
    print("Error Message Bar: Product identifier isn't correct? Please try again!") #List append() REFERENCE : https://www.youtube.com/watch?v=3BaGb-1cIr0&feature=youtu.be
print("SHOPPING CARD IDENTIFIERS INCLUDE:",(product_ids)) 

product_total = 0
for product_id in product_ids:
  matching_products = [p for p in products if str(p["id"]) == str(product_id)]
  matching_product = matching_products[0]                 #List append() REFERENCE : https://www.youtube.com/watch?v=3BaGb-1cIr0&feature=youtu.be
  
  
  usd = "${0:.2f}".format(matching_product["price"])      #usd format REFERENCE :https://www.youtube.com/watch?v=Noy20XaMqho&feature=youtu.be
  print(" + " + matching_product["name"] + " (" + str(usd) + ")")

  usd2 = "${0:.2f}".format(product_total) 
  product_total += matching_product["price"]
  
  tax_total = (product_total * 8.75)/100
  usd3 = "${0:.2f}".format(tax_total)  
  
  grand_total = product_total + tax_total
  usd4 = "${0:.2f}".format(grand_total) 
  
print("---------------------------------")
print("SUBTOTAL:" + str(usd2))
print("NY SALES TAX:" + str(usd3))
print("TOTAL:" + str(usd4))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")