from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["great", "greater", "greatest"]

stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)