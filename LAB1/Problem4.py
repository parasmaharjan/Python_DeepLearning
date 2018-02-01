def main():
    print('Program started...')
    py_file = open('Python_Students.txt','r')
    py_students = []
    for line in py_file:
        py_students.append(line.strip('\n'))
        #print(line)
    #print(py_students)
    web_file = open('Web_Students.txt', 'r')
    web_students = []
    for line in web_file:
        web_students.append(line.strip('\n'))
    #print(web_students)
    classify(py_students,web_students)

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


    print('Students in both classes: ')
    print(both)
    print('Students in python class: ')
    print(py_only)




# def py_only(p,w):
#
# def web_only(p,w):
#

if __name__ == "__main__":
    main()
    #test()