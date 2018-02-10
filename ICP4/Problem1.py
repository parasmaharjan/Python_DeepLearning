# Employee class
class Employee:
    count = 0
    emp_list = []

    #  constructor
    def __init__(self):
        #print(self.emp_list)
        #Employee.count += 1
        pass

    def addEmployee(self, first, last, pay, department):
        Employee.emp_list.append([first, last, pay, department])

    def getInfoEmployee(self):
        return Employee.emp_list

    def getAvgSalary(self):
        self.sum = 0
        for i in range(Employee.getNumEmployee(self)):
            self.sum += Employee.emp_list[i][2]
        return self.sum/Employee.getNumEmployee(self)

    def getNumEmployee(self):
        return len(Employee.emp_list)


employee = Employee()

employee.addEmployee('paras', 'maharjan', 30000, 'RnD')
employee.addEmployee('sarap', 'maharjan', 50000, 'Accounts')

emp_list = employee.getInfoEmployee()
print('First name\tLast name\tSalary($)\tDepartment')
print('----------------------------------------------')
for i in range(employee.getNumEmployee()):
    print('{}\t\t{}\t{}\t\t{}'.format(emp_list[i][0], emp_list[i][1], emp_list[i][2], emp_list[i][3]))

print('Total number of employee: ', employee.getNumEmployee())
print('Average salary of employee: ', employee.getAvgSalary())


