magicians = ["ejiro", "ifeco", "kingsley", "samuel"]
for magician in magicians:
 print(magician)
 print(f"{magician.title()}, that was a good performance!")
 print(f"i cant wait to see you at the party, {magician.title()}.\n")
print("thank you, everyone that was a great show!") 
for value in range(1, 5):
 print(value)
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
squares = []
for value in range(1, 12):
 square = value ** 2
 squares.append(square)
print(squares)
multiples = []
for value in range(2, 10):
 multiples.append(value ** 2) 
print(multiples)
players = ["charles", "godwin", "emeka", "ifeanyi", "judith"]
print(players[0:2])
print(players[2:])
print(players[-3:])
print("here are the 1st 3 players in my team:")
for player in players[-3:]:
 print(player.title())
my_food = ["egusi", "ogbono", "rice", "beans"]
friends_food = my_food
print("my favorite food are:")
print(my_food)
print("\nmy friend favorite foods are:")
print(friends_food)
my_food.append("jollof")
print(my_food)
