import nltk
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk
from nltk.tokenize import wordpunct_tokenize
from collections import Counter
from operator import itemgetter
def main():
    with open("Text.txt", 'r') as file:
        content = file.read()
    #print(content)

    # file = open("Text.txt", 'r')
    # content = file.readline()
    # content = "Hi my name is paras. My name is also refered as parash. I live in Patan."
    print(content)

    tokens = nltk.word_tokenize(content)
    print(tokens)

    lemmatizer = WordNetLemmatizer()
    lemmatize_word = []
    for words in tokens:
        lemmatize_word.append(lemmatizer.lemmatize(words))

    bi_word = []
    for w1, w2 in nltk.bigrams(lemmatize_word):
        bi_word.append([w1, w2])
    print(bi_word)

    #print([[i, j, sum({i, j}.issubset(k) for k in bi_word)] for i, j in bi_word])

    bi_word_counter = Counter(tuple(r) for r in bi_word)

    new = list(sorted(bi_word_counter.items(), key=itemgetter(1), reverse=True)[:5])

    print(new)
    n = []
    for i in range(0,len(new)):
        n.append(new[i][0])
    print(n)

    sentences = nltk.sent_tokenize(content)

    for sent in sentences:
        tokens = nltk.word_tokenize(sent)
        lemmatize_word = []
        for words in tokens:
            lemmatize_word.append(lemmatizer.lemmatize(words))
        bi_word = []
        for w1, w2 in nltk.bigrams(lemmatize_word):
            #bi_word.append((w1, w2))
            if (w1, w2) in n:
                print(sent)
                break
        #print(bi_word)



if __name__ == '__main__':
    print("LAB 3 - Problem 3")
    main()



