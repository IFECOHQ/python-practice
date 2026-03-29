names = ['promise', 'ejiro', 'samuel']
print(names[-2])
print(names[1].title())
message = f"my name is {names[1].title()}"
print(message)
names[1] = "ifeanyi"
print(names)
names.append("kingsley")
print(names)
names.insert(1, "ifeco")
print(names)
del(names[1])
print(names)
popped_names = names.pop(1)
print(names)
print(popped_names)
last_name = names.pop(1)
print(f"the last name that was called is {last_name.title()}")
too_old = "promise"
names.remove(too_old)
print(names)
print(f"\n{too_old.title()} is too old for me")
bignames = ["ejiro", "ifeco", "kingsley", "promise"]
bignames.sort(reverse=True)
print(bignames)
cars = ["bmw", "audi", "benz", "toyota"]
print(cars)
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)
len(cars)
print(cars[1])