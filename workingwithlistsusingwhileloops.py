uncomfirmed_users = ['emeka', 'john', 'ifeco']
comfirmed_users = []
while uncomfirmed_users:
    current_users = uncomfirmed_users.pop()

    print(f"verifying user: {current_users.title()}")
    comfirmed_users.append(current_users)
    print("\nthe following users has  been verified: ")
    for comfirmed_user in comfirmed_users:
        print(comfirmed_user.title())
print(comfirmed_users)

pronouns = ['me', 'us', 'them', 'me', 'me']
print(pronouns)
while 'me' in pronouns:
    pronouns.remove('me')
print(pronouns)    