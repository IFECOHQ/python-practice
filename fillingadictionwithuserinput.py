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
# first you would create a list for orders and an empty list for finished orders
sandwich_orders = ['beans', 'rice', 'fiofio']
finished_sandwiches = []
# loop through sandwich_orders until the list is empty
while sandwich_orders:
    # write a code to remove the last order from the first list and append to finished orders
    current_orders = sandwich_orders.pop()
    print(f"verifying users: {current_orders.title()}")  
    finished_sandwiches.append(current_orders) 
    print("the following users has been verified")
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich.title())
print(finished_sandwiches)

# this is another exercise
('the deli has run oot of ejiro')
sandwich_orderrs = ['beans', 'rice', 'fiofio', 'ejiro', 'ejiro', 'ejiro']
finished_sandwichers = []
while 'ejiro' in sandwich_orderrs:
    sandwich_orderrs.remove('ejiro')
    print(sandwich_orderrs)
while sandwich_orderrs:
    # write a code to remove the last order from the first list and append to finished orders
    current_orderrs = sandwich_orderrs.pop()
    print(f"verifying users: {current_orderrs.title()}")  
    finished_sandwichers.append(current_orderrs) 
    print("the following users has been verified")
    for finished_sandwichr in finished_sandwichers:
        print(finished_sandwich.title())
print(finished_sandwichers)

