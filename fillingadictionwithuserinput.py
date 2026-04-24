responses = {}
# set a flag to indicate that polling is active
polling_active = True
while polling_active:
    name = input('pls type in your name')
    response = input('which mountain would you like to visit')
    # store the resonse in a dictionary
    responses[name] = response
    # find out if anyone else is going to take the poll
    repeat = input('will anyone else like to take the poll')
    if repeat == 'no':
        polling_active = False
# polling is complete. show the results.
print('\n--- poll results ---')
for name, response in responses.items():
    print(f'{name} would like to climb {response}')

# this is an exercise
sandwich_orders = ['beans', 'rice', 'fiofio']
finished_sandwiches = []
while sandwich_orders:
    current_orders = sandwich_orders.pop()
    print(f"verifying users: {current_orders.title()}")  
    finished_sandwiches.append(current_orders) 
    print("the following users has been verified")
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich.title())
print(finished_sandwiches)           

