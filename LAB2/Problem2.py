# Creating list of contacts
contact_list = []


class Contact:

    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
        contact_list.append([self, self.name, self.number])

    def display_name(self):
        return self.name

    def display_number(self):
        return self.number

    def display_email(self):
        return self.email

    # For update info
    def update(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email


def display_all():
    print('')
    print('Name\tNumber\t\t\tEmail')
    print('---------------------------------')
    for contact in contact_list:
        print(contact[0].display_name(), '\t', contact[0].display_number(), '\t', contact[0].display_email())
    print('')


def display_by_name(search_name):
    for contact in contact_list:
        # print(contact)
        if contact[1] == search_name:
            print('')
            print('Name: ', contact[0].display_name())
            print('Number: ', contact[0].display_number())
            print('Email: ', contact[0].display_email())
            break


def display_by_number(search_number):
    for contact in contact_list:
        # print(contact)
        if contact[2] == search_number:
            print('')
            print('Name: ', contact[0].display_name())
            print('Number: ', contact[0].display_number())
            print('Email: ', contact[0].display_email())
            break


def edit_by_name(old_name, new_name, new_number, new_email):
    # Check if name or contact already exist
    for contact in contact_list:
        if (new_name in contact) | (new_number in contact):
            print('')
            print("Name or Number already exist")
            break

    # Find the index of the old name and replace it with the new info
    for idx, contact in enumerate(contact_list):
        if contact[1] == old_name:
            contact[0].update(new_name, new_number, new_email)
            contact_list[idx][1] = new_name
            contact_list[idx][2] = new_number

    display_all()


def main():
    # Creating the instance of class Contact
    contact_1 = Contact('Paras', '9849xxxxxx', 'paras.maharjan@gmail.com')
    contact_2 = Contact('Sushma', '9860xxxxxx', 'sushma.maharjan@gmail.com')
    contact_3 = Contact('Sarap', '9861xxxxxx', 'sarap.maharjan@gmail.com')

    while True:
        print('')
        print('0. Display all contact list')
        print('1. Display contact by name')
        print('2. Display contact by number')
        print('3. Edit contact by name')
        print('4. Exit\n\r')

        option = input("Select any of the above: ")
        print('')

        if option == '0':
            display_all()

        elif option == '1':
            name = input('Search name: ')
            display_by_name(name)

        elif option == '2':
            number = input('Search number: ')
            display_by_number(number)

        elif option == '3':
            old_name = input('Enter old name: ')
            new_name = input('Enter new name: ')
            new_number = input('Enter new number: ')
            new_email = input('Enter new email: ')
            print('')

            edit_by_name(old_name, new_name,new_number, new_email)

        else:
            exit()


def test():
    contact_1 = Contact('Paras', '9849xxxxxx', 'paras.maharjan@gmail.com')
    contact_2 = Contact('Sushma', '9860xxxxxx', 'sushma.maharjan@gmail.com')

    display_by_name('Paras')
    edit_by_name('Paras', 'Sarap', '9861xxxxxx', 'sarap.maharjan@gmail.com')
    display_by_number('9860xxxxxx')


if __name__ == "__main__":
    main()
    #test()
