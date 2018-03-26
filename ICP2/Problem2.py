file = open("Text.txt", 'r')
line = file.readline()
while line != "":
    length = len(line)
    print(length)
    line = file.readline()
