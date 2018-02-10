'''
Set and Dictionary
'''

def main():
    str = input("Enter any string: ")
    count_word(str)
    count_vowel(str)

def test():
    str = 'hello world this is my first hello'
    count_word(str)
    count_vowel(str)

def count_word(str):
    list = str.split()
    d = {x: list.count(x) for x in list}
    print(d)

def count_vowel(str):
    vowel_set = {'a','e','i','o','u','A','E','I','O','U'}
    count = 0
    for letter in str:
        if letter in vowel_set:
            count = count+1
    print('Vowel count: ', count)

if __name__ == "__main__":
    main()
    #test()
