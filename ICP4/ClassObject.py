# Python Object-Oriented Programming
# attribute - data
# method - function associated with class

# Employee class

class Employee:

    # special init method - as initialize or constructor
    # self == instances
    def __init__(self, first, last, pay, department):
        self.first = first
        self.last = last
        self.pay = pay
        self.department = department

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

# Instance variable
emp_1 = Employee('Paras','Maharjan', 50000, 'RnD')
#print(emp_1)
emp_2 = Employee('Sarap', 'Maharjan', 70000, 'Accounts')
#print(emp_2)

# print(emp_1.first, ' ', emp_1.last, ', ', emp_1.department, ', ', emp_1.pay)
# print(emp_2.first, ' ', emp_2.last, ', ', emp_2.department, ', ', emp_2.pay)

# print using place holder
print('First name\tLast name\tSalary($)\tDepartment')
print('----------------------------------------------')
print('{}\t\t{}\t{}\t\t{}'.format(emp_1.first, emp_1.last, emp_1.pay, emp_1.department))
print('{}\t\t{}\t{}\t\t{}'.format(emp_2.first, emp_2.last, emp_2.pay, emp_2.department))

# class instance is pass argument to method, so we need to use self
# print(Employee.fullname(emp_1))
# print(emp_2.fullname())




