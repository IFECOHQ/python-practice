people = {
    'ezeja': {
        'first': 'ezeja',
        'last': 'john',
        'location': 'enugu'
          },
    'ifeco': {
        'first': 'ifeanyi',
        'last': 'kingsley',
        'location': 'awka',
    }      
}
for username, user_info in people.items():
    print(f'username: {username}')
    full_name = f'{user_info['first']} {user_info['last']}'
    location = user_info['location']

    print(f'\tfullname: {full_name.title()}')
    print(f'\tlocation: {'location'}')

name = input('pls input your name') 
print(f'hello, {name}')    
    
