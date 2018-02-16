# Airline Reservation System
# Create empty list of Employee class
employee_info = []
# Create list of Flight class
flight_list = []


class Person:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def get_person_info(self):
        return [self.name, self.contact]

    def update_person_info(self, name, contact):
        self.name = name
        self.contact = contact


class Payment:

    def __init__(self, currency, payment):
        # dollar = 0, pound = 1
        self.currency = currency
        self.payment = payment

    def get_payment_info(self):
        return [self.currency, self.payment]

    def update_payment_info(self, currency, payment):
        self.currency = currency
        self.payment = payment


class Passenger(Person, Payment):

    def __init__(self, name, contact, currency, payment, status):
        Person.__init__(self, name, contact)
        Payment.__init__(self, currency, payment)
        self.status = status

    def get_passenger_info(self):
        return [self.status]

    def update_passenger_info(self, status):
        self.status = status


# Inherit Passenge class
class Flight(Passenger):

    def __init__(self, name, contact, currency, payment, status, flight_no, departure, arrival):
        # Call super class
        super().__init__(name, contact, currency, payment, status)
        self.flight_no = flight_no
        self.departure = departure
        self.arrival = arrival

    def get_flight_info(self):
        return [self.flight_no, self.departure, self.arrival]


# Inherit two class
class Employee(Person, Payment):

    def __init__(self, name, contact, currency, payment, status):
        Person.__init__(self, name, contact)
        Payment.__init__(self, currency, payment)
        self.status = status
        # Private data member. Can only be access within class
        self.__bonus = 0
        if self.status == 1:
            self.__bonus = 200


    def get_employee_info(self):
        # Accessing private member within class
        return [self.status, self.__bonus]


def display_all_employee():
    print('\r\nEmployee Info...\r\n')
    print('Name\tContact\t\t\tCurency\t\tSalary\tSatus\t\tBonus')
    print('----------------------------------------------------------------')
    for emp in employee_info:
        print(emp.get_person_info()[0], '\t', \
                emp.get_person_info()[1], '\t', \
                ('Dollar' if emp.get_payment_info()[0] == 0 else 'Pound '), '\t', \
                emp.get_payment_info()[1], '\t', \
                ('Temporary' if emp.get_employee_info()[0] == 0 else 'Fulltime'), '\t', \
                emp.get_employee_info()[1])
        print('')


def display_all_flight():
    print('\n\rFlight Info...\r\n')
    print('Name\tContact\t\t\tCurrency\tCost\tStatus\t\tFlight No\tDeparture\tArrival')
    print('--------------------------------------------------------------------------------------------')
    for flt in flight_list:
        print(flt.get_person_info()[0],'\t', \
              flt.get_person_info()[1], '\t', \
              ('Dollar' if flt.get_payment_info()[0] == 0 else 'Pound '),'\t', \
              flt.get_payment_info()[1], '\t', \
              ('Economy' if flt.get_passenger_info()[0] == 0 else 'Business'), '\t', \
              flt.get_flight_info()[0], '\t', \
              flt.get_flight_info()[1], '\t', \
              flt.get_flight_info()[2]);
        print('')


def update_passenger_info(old_name, name, contact, status):
    print("Edit by name....")
    # Search entry by name
    for flt in flight_list:
        if old_name in flt.get_person_info():
            flt.update_person_info(name, contact)
            flt.update_passenger_info(status)
    display_all_flight()


def search_passenger(name):
    print("Searching by name....")
    # Search entry by name
    for flt in flight_list:
        if name in flt.get_person_info():
            print('Name: ', flt.get_person_info()[0])
            print('Contact: ', flt.get_person_info()[1])
            print('Currency: ', ('Dollar' if flt.get_payment_info()[0] == 0 else 'Pound'))
            print('Cost: ', flt.get_payment_info()[1])
            print('Status: ', ('Economy' if flt.get_passenger_info()[0] == 0 else 'Business'))
            print('Flight No: ', flt.get_flight_info()[0])
            print('Departure Address: ', flt.get_flight_info()[1])
            print('Arrival Address: ', flt.get_flight_info()[2])
            print('')


def main():
    # Create instance for Employee class
    employee_info.append(Employee("Paras", '9849654321', 0, 1000, 0))
    employee_info.append(Employee("Sarap", '9849567890', 1, 2000, 1))

    # Create instance for Flight class
    flight_list.append(Flight('Sushma', '9860123456', 0, 300, 0, 'BOING123', 'Kathmandu', 'Kansas City'))
    flight_list.append(Flight('Amhsus', '9818987654', 1, 500, 1, 'BOING567', 'Kathmandu', 'Paris'))


    # Creating insance for Person
    person = Person('Smith', '9847888999')
    print(person.get_person_info())
    print('')

    # Creating instance for Payment
    payment = Payment(1, 100)
    print(payment.get_payment_info())
    print('')

    # Creating instance for Passenger
    passenger = Passenger('John', '9803012012', 0, 500, 1)
    print(passenger.get_person_info())
    print(passenger.get_payment_info())
    print(passenger.get_passenger_info())


    while True:
        print('')
        print('1. Display all Employee list')
        print('2. Display all Flight list')
        print('3. Search Passenger by name')
        print('4. Update Passenger info')
        print('5. Exit\n\r')

        option = input("Select any of the above: ")
        print('')

        if option == '1':
            display_all_employee()

        elif option == '2':
            display_all_flight()

        elif option == '3':
            search_name = input('Search name: ')
            search_passenger(search_name)

        elif option == '4':
            old_name = input('Enter old name: ')
            new_name = input('Enter new name: ')
            new_contact = input('Enter new contact: ')
            new_status = input('Enter new status: ')
            print('')

            update_passenger_info(old_name, new_name, new_contact, new_status)

        else:
            exit()


if __name__ == '__main__':
    main()