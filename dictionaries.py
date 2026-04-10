alien_0 = {"colour": "green", "x_position": 0, "y_position": 25, "speed": "medium", "points": 5}
print(alien_0)
# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3
# the new position is the old position plus the new position
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"\nnew position: {alien_0["x_position"]}") 
del alien_0["points"]  
print(alien_0) 
favourite_languages = {
    "macoll": "c",
    "princess": "python",
    "fabet": "rust",
}
language = favourite_languages["macoll"].title()
print(f"macolls favorite language is {language}.")
point_value = alien_0.get("points", "No points assigned")
print(point_value)

user_0 = {
    "first": "ebuka",
    "last": "ada",
    "username": "ifeco",
}
for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for participating")

print("\nthe following languages have been taken:") 
for language in favourite_languages.keys():
    print(language.title())

alien_1 = {"color": "blue", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# make an empty list of monsters
monsters = []
# make 30 new monsters 
for monster_number in range(20):
    new_monster = {"colour": "pink", "speed": "fast", "points": 6}
    monsters.append(new_monster)
for monster in monsters[:5]:
    print(monster)
for monster in monsters[:3]:
    if monster["colour"] == "pink":
        monster["colour"] = "violet"
        monster["speed"] = "medium"
        monster["points"] = "15"
for monster in monsters[:5]:
    print(monster)      

