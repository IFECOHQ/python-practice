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
requestedd_toppings = ["mushrooms", "extra cheese"] 
if "mushrooms" in requestedd_toppings:
    print("\nadding mushroom")  
if "extra cheese" in requestedd_toppings:
    print("adding extra cheese")
if "pepperoni" in requestedd_toppings:
    print("adding pepperoni")  
print("\nfinished making your pizza")
available_toppings = ["shoe", "car", "cake", "peanut", "sugar"]
requested_toppings = ["car", "cake", "juice"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping}")
    else:
        print(f"sorry, we don't have {requested_topping}") 
requested_cars = []  
if requested_cars:
    for requested_car in requested_cars:
        print(f"adding {requested_car}!")
else:
        print("are you sure you don't want a car")   
