import urllib.request
from bs4 import BeautifulSoup
import os
import nltk
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk
from nltk.tokenize import wordpunct_tokenize


def main():
    web_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    wiki_request = urllib.request.urlopen(web_url)
    wiki_parse = BeautifulSoup(wiki_request, "html.parser")

    print("\nFirst Paragraph\n")
    web_para = wiki_parse.find('p')
    #print(web_para.text)
    file = open("text.txt", 'w')
    file.write(str(web_para.text))

    print("\nWord Tokenizing\n")
    tokens = nltk.word_tokenize(web_para.text)
    print(tokens)

    print("\nSentence Tokenizing\n")
    sentence = nltk.sent_tokenize(web_para.text)
    print(sentence[0])

    print("\nPart of speech\n")
    tagged = nltk.pos_tag(tokens)
    print(tagged[0:6])

    print("\nStemming\n")
    stermmer = PorterStemmer()
    for word in tokens[1:11]:
        print(word + " : " + stermmer.stem(word))

    print("\nLemmatizing\n")
    lemmatizer = WordNetLemmatizer()
    for word in tokens[1:11]:
        print(word + " : " + lemmatizer.lemmatize(word))

    print("\nBest Lemmatizing Example: cacti - ", lemmatizer.lemmatize("cacti"))

    print("\nN-gram\n")

    for w1, w2, w3 in nltk.trigrams(wordpunct_tokenize(sentence[2])):
        print(w1, w2, w3)

    print("\nName entity\n")
    for sent in sentence[0:2]:
        print(ne_chunk(nltk.pos_tag(wordpunct_tokenize(sent))))


if __name__ == "__main__":
    main()





