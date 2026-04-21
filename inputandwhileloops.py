current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 
prompt = "\ntell me something, and i will say it back to you:" 
prompt += "\nenter 'quit' to end the program." 
message = ""
while message != 'quit':  
    message = input(prompt) 
    print(message)
    if message != 'quit':
        print(message)
active = True
while active:
    message = input(prompt)
    if message == "quit" :
        active = false
    else:
        print(message)          