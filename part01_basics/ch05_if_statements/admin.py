curr_users = ['John', 'Geqian', 'Tequila', 'Admin']
new_users = ['haha', 'Xiyang', 'TEQUILA', 'geqian']

if curr_users:
    for user in curr_users:
        if user.lower() == 'admin':
            print('Welcome, my master.')
        else:
            print('Welcome to use my system.')
else:
    print('We need to find some users.')


curr_users_lower = []
for user in curr_users:
    curr_users_lower.append(user.lower())
# print(curr_users_lower)

for user in new_users:
    if user.lower() in curr_users_lower:
        print("Your username has been used!")
    else:
        print("Welcome, new user~")




