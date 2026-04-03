age = 12
if age < 4:
    print("your admission cost is 0$")
elif age < 18:
    print("your admission cost is 5$")   
else:
    print("your admission cost is 12$") 
age = 13
if age < 4:
    price = 0
elif age < 18:
    price = 15
else: 
    price = 50  
print(f"\nyour admission cost is {price}.") 
requested_toppings = ["mushrooms", "extra cheese"] 
if "mushrooms" in requested_toppings:
    print("\nadding mushroom")  
if "extra cheese" in requested_toppings:
    print("adding extra cheese")
if "pepperoni" in requested_toppings:
    print("adding pepperoni")  
print("\nfinished making your pizza")
