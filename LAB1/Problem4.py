'''
    Date: Feb 1, 2018
    Author: Paras Maharjan
    Class: Pyhton and Deep Learning
    Lab Assignment: 1
    Problem: 4

    Consider the following scenario. You have a list of students who are attending class “Python” and another list of
    students who are attending class “Web Application”. Find the list of students who are attending both the classes.
    Also find the list of students who are not common in both the classes. Print it.

'''

def main():
    print('Program started...')

    # Open file of students from Python class
    py_file = open('Python_Students.txt','r')

    py_students = []
    for line in py_file:
        py_students.append(line.strip('\n'))
    #print(py_students)

    # Open file of students from Python class
    web_file = open('Web_Students.txt', 'r')
    web_students = []
    for line in web_file:
        web_students.append(line.strip('\n'))
    #print(web_students)

    # Call the function classify()
    classify(py_students,web_students)

# This function classifies the students common in both class and students only in Python and only in Web class
def classify(p,w):
    both = []
    py_only = []
    web_only = []
    for name in p:
        if name in w:
            #print('Both: ',name)
            both.append(name)
        else:
            #print('Python: ', name)
            py_only.append(name)
    for name in w:
        if name not in both:
            web_only.append(name)

    print('Students in both classes: ')
    print(both)
    print('Students only in python class: ')
    print(py_only)
    print('Students only in web class: ')
    print(web_only)

if __name__ == "__main__":
    main()

