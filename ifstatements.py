cars = ["audi", "bmw", "toyota", "camry"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())  
    if car == "toyota":  
        print("this is a Toyota!") 
    else:
        print("these are all nice cars!")
cars.append("benz")
print(cars)      
                