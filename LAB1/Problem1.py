'''
    Date: Feb 1, 2018
    Author: Paras Maharjan
    Class: Pyhton and Deep Learning
    Lab Assignment: 1
    Problem: 1

    For any web application login, the user password need to be validated against database rules. For My UMKC web
    application following are the criteria for valid password:
    a)	The password length should be in range 6-16 characters
    b)	Should have at least one number
    c)	Should have at least one special character in [$@!*]
    d)	Should have at least one lowercase and at least one uppercase character
'''

import string

def main():
    print('Program started...')
    # display information about the program
    print('Program to check if the input password is valid or not')
    print('a)	The password length should be in range 6-16 characters\n\r'\
            'b)	Should have at least one number\n\r'\
            'c)	Should have at least one special character in [$@!*]\n\r'\
            'd)	Should have at least one lowercase and at least one uppercase character\n\r\n\r')

    # Input username
    username = get_username()
    # Input password
    password = get_password(username)

    # Check for validation of the password
    validate(username, password)

# Creating testing function to test program with default username and password
def test():
    password = 'Paras0@'
    username = 'paras'
    #call validate function to check the validation on password
    validate(username, password)

def validate(un, pw):

    # Using the Status flag to maintain the validation of password through
    status = 1

    len(pw)
    # Check if the password length is grater than or equal to 6
    if len(pw) < 6 or len(pw) > 16:
        status = 0
        print('Password length should be in range of 6-16 character')

    # Check if password is equal to username
    if un is pw:
        status = 0
        print('Username and password cannot be same')

    # Check if presence of at least one lower case alphabet
    if len(set(string.ascii_lowercase).intersection(pw)) < 1:
        status = 0
        print("Password need at least one lowercase alphabet a-z")

    # Check if presence of at least one upper case alphabet
    if len(set(string.ascii_uppercase).intersection(pw)) < 1:
        status = 0
        print("Password need at least one uppercase alphabet A-Z")

    # Check if presence of at least one digit
    if len(set(string.digits).intersection(pw)) < 1:
        status = 0
        print("Password must contain at least one digit 0-9")

    # Check if presence of at least one special character [!@$*]
    if not ((len(set(string.punctuation[0]).intersection(pw)) > 0) or\
            (len(set(string.punctuation[3]).intersection(pw)) > 0) or\
            (len(set(string.punctuation[9]).intersection(pw)) > 0) or\
            (len(set(string.punctuation[21]).intersection(pw)) > 0)):
        status = 0
        print("Password must contain at least one special character [ !$@* ]")
    if status is 1:
        print("Password is valid!")
    else:
        print("Password is invalid!")

# This function takes the username as input from the user
def get_username():
    username = input('Username: ')
    return username

# This function takes the password as input from user
def get_password(username):
    password = input('Password: ')
    return password

if __name__ == "__main__":
    main()
    #test()