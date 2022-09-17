# Basic login and signup form

print("Create account now...")

username = input('Enter your new username here...\n')
password = input('Enter your password here...\n')

print('Account created successfully...')
print('\n Login with your username and password')

username1 = input('Username \n')
password1 = input('Passsword \n')

if username == username1 and password == password1:
    print("Login successfull...")
else:
    print('Invalid Credentials')