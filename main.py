from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import math

print("Hi, how can we help you?")
x = input()

sw = stopwords.words('english')
# print(sw)


question_vectors = []

ranks = []
for idx, question in enumerate(questions):
    l1 = []
    l2 = []
    temp = word_tokenize(question)
    question_vectors.append(temp)

    user = word_tokenize(x)

    # remove stop words from the string
    temp_set = {w for w in temp}  # if not w in sw}
    print(temp_set)
    user_set = {w for w in user}  # if not w in sw}
    print(user_set)

    # form a set containing keywords of both strings
    rvector = temp_set.union(user_set)
    for w in rvector:
        if w in user_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if w in temp_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0

    # cosine formula
    for i in range(len(rvector)):
        c += l1[i]*l2[i]
    cosine = c / ((sum(l1)**0.5*(sum(l2))**0.5))
    print("similarity: ", cosine)
    ranks.append((idx, cosine))

ranks.sort(key=lambda y: y[1], reverse=True)
print()
print(ranks)
print()
print("==Answer One:==")
print(answers[ranks[0][0]])
print()
print("==Answer Two:==")
print(answers[ranks[1][0]])
