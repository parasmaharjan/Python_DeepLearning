import string


def main():
    print('Program started...')
    username = get_username()
    password = get_password(username)
    validate(username, password)

def validate(un, pw):
    len(pw)
    if len(pw) < 6 or len(pw) > 16:
        print('Password length should be in range of 6-16 character')
    if un is pw:
        print('Username and password cannot be same')
    if len(set(string.ascii_lowercase).intersection(pw)) < 1:
        print("Password need at least one lowercase alphabet a-z")
    if len(set(string.ascii_uppercase).intersection(pw)) < 1:
        print("Password need at least one uppercase alphabet A-Z")
    if len(set(string.digits).intersection(pw)) < 1:
        print("Password must contain at least one digit 0-9")
    if not ((len(set(string.punctuation[0]).intersection(pw)) > 0) or (len(set(string.punctuation[3]).intersection(pw)) > 0) or (len(set(string.punctuation[9]).intersection(pw)) > 0) or (len(set(string.punctuation[21]).intersection(pw)) > 0)):
        print("Password must contain at least one special character [ !$@* ]")
    else:
        print('Valid')
        return

#this function takes the username as input from the user
def get_username():
    username = input('Username: ')
    return username

#this function takes the password as input from user
def get_password(username):
    password = input('Password: ')
    return password

#creating testing function to test program with default username and password
def test():
    password = 'Paras0@'
    username = 'paras'
    #call validate function to check the validation on password
    validate(username, password)

if __name__ == "__main__":
    main()
    #test()