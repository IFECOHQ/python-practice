cars = ["bmw", "toyota", "benz"]
for car in cars:
    if car == "Bmw":
        print(cars)
    else:
        print("these are not bmw's!")    
requested_toppings = "mushrooms"
if requested_toppings != "anchovies":
    print("hold the anchovies")
answer = 18
if answer != 42:
    print("that is not the correct answrr, pls try again!")
age_0 = 18
age_1 = 16
if age_0 >= 21 and age_1 >= 21:
    print("you are not eligible!")
else:
    print("you are eligible!")  
banned_users = ["promise", "samuel", "emeh", "ike"] 
user = "kingsley" 
if user not in banned_users:
    print(f"{user.title()}, you can make a response")
else:
    print("you have been banned")
age = 18
if age >= 21:
    print("\nyou are eligible to vote")
    print("have you registered?")
