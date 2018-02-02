'''
    Date: Feb 1, 2018
    Author: Paras Maharjan
    Class: Pyhton and Deep Learning
    Lab Assignment: 1
    Problem: 2

    Write a Python function that accepts a sentence of words from user and display the following:
    a)	Middle word
    b)	Longest word in the sentence
    c)	Reverse all the words in sentence

'''

def main():
    print("Program started...")
    # Displays the information about the program
    print('Program to display middle word, longest word in sentence and reverse all the words in sentence\n\r')
    str = input("Enter any string: ")
    task(str)

def test():
    print("Test Program started...")
    str = "hello my name is Paras Maharjan"
    task(str)

def task(str):
    list = str.split()
    #print(list)

    # task 1
    length = len(list)
    #print(length)
    residue = len(list) % 2
    #print(residue)
    if residue > 0:
        print('[', list[int((length) / 2)], ']')
    else:
        print('[', list[int(length / 2) - 1], ',', list[int(length / 2)], ']')

    # task 2
    longest_word = ''
    length = 0
    for word in list:
        # print(word,',',len(word))
        if len(word) > length:
            length = len(word)
            longest_word = word
    print('Longest word: ', longest_word)

    #task 3
    reverse_list = []
    for word in list:
        reverse_list.append(word[::-1])
    # Join the reversed word to form a sentence
    print(' '.join(word for word in reverse_list))

if __name__ == "__main__":
    main()
    #test()