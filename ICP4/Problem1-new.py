class Employee:
    emp_list = []
    count = 0

    def __init__(self, first, last, pay, department):
        self.first = first
        self.last = last
        self.pay = pay
        self.department = department
        Employee.emp_list.append([first, last, pay, department])
        Employee.count += 1

    # This function takes the average of the salary
    def getAvgSalary(self):
        sum = 0
        for i in range(Employee.getNumEmployee(self)):
            sum += Employee.emp_list[i][2]
        return sum/Employee.getNumEmployee(self)

    def getNumEmployee(self):
        return Employee.count
        #return len(Employee.emp_list)

    def getInfoEmployee(self):
        print('{}\t\t{}\t{}\t\t{}'.format(self.first, self.last, self.pay, self.department))


class FulltimeEmployee(Employee):
    def __init__(self, first, last, pay, department, bonus):
        self.bonus = bonus
        pay = pay + bonus
        Employee.__init__(self, first, last, pay, department)

    def getInfoFulltimeEmployee(self):
        salary = self.pay - self.bonus
        print('{}\t\t{}\t{}\t\t{}\t\t{}'.format(self.first, self.last, salary, self.department, self.bonus))

if __name__=="__main__":
    print('New program started!')

    a = Employee('paras','maharjan',10000,'rnd')
    b = Employee('sarap', 'maharjan', 10000, 'accounts')

    c = FulltimeEmployee('sushma', 'maharjan', 10000, 'analyst', 0)

    print('\r\nFirst name\tLast name\tSalary($)\tDepartment')
    a.getInfoEmployee()
    b.getInfoEmployee()

    print('\r\nFirst name\tLast name\tSalary($)\tDepartment\tBonus')
    c.getInfoFulltimeEmployee()
    print('\r\nAverage salary: ', Employee.getAvgSalary(0))
