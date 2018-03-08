import nltk
from nltk.stem import WordNetLemmatizer
from collections import Counter
from operator import itemgetter


def main():
    with open("Text.txt", 'r') as file:
        content = file.read()

    # Print the content of file
    print(content, "\n\r")

    # List the tokens ie. each word
    tokens = nltk.word_tokenize(content)
    # print(tokens)

    # Applying the lemmatization on tokens
    lemmatizer = WordNetLemmatizer()
    lemmatize_word = []
    for words in tokens:
        lemmatize_word.append(lemmatizer.lemmatize(words))

    # Applying Bi-gram in lemmatize data
    bi_word = []
    for w1, w2 in nltk.bigrams(lemmatize_word):
        bi_word.append([w1, w2])
    #print(bi_word)

    # Finding the number of repetition and arrange in descending order
    bi_word_counter = Counter(tuple(r) for r in bi_word)

    # Taking the top 5 Bi-gram
    top_bi_gram = list(sorted(bi_word_counter.items(), key=itemgetter(1), reverse=True)[:5])
    #print(top_bi_gram, "\n")

    # Removing the count column
    top_bi_gram_ = []
    print("Top Bi-grams:")
    for i in range(0, len(top_bi_gram)):
        top_bi_gram_.append(top_bi_gram[i][0])
        print(top_bi_gram[i])
    print("")

    # Tokenize the sentences
    sentences = nltk.sent_tokenize(content)

    print("\nSummarised text: \n")
    # Finding the sentences with top Bi-gram
    for sent in sentences:
        tokens = nltk.word_tokenize(sent)
        lemmatize_word = []
        for words in tokens:
            lemmatize_word.append(lemmatizer.lemmatize(words))
        for w1, w2 in nltk.bigrams(lemmatize_word):
            if (w1, w2) in top_bi_gram_:
                print(sent)
                break


if __name__ == '__main__':
    print("LAB 3 - Problem 3\nSummerize the text using nltk\n")
    main()



