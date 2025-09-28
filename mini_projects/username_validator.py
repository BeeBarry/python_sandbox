# Validating the following:
# 1. username does not contain more than 12 characters.
# 2. username does not contain whitespaces.
# 3. username does not contain digits.

username = input('Enter your username: ')

if len(username) > 12:
    print('Error! Your username can not contain more than 12 characters.')
elif not username.find(' ') == -1:
    print('Error! Your username cannot contain whitespace.')
elif not username.isalpha():
    print('Error! Your username can not contain numbers')
else:
    print(f'Success! Welcome {username}!')