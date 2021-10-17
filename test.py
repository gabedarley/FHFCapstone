from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np


questions = ['What is an IEP?', 'What is an LEA?', 'What is IDEA?', 'Should I have my child evaluated for special education?']

answers = ['IEP is an individualized Education Program that provides a written plan designed to meet the unique needs of the child with an exceptionality.', 'LEA is the local education agency, also referred to as the local school district.', 'IDEA is the Individuals with Disabilities Education Act, the Federal special education law that guarantees FAPE.']

print("Hi, how can we help you?")
x = input()

sw = stopwords.words('english')
print(sw)
l1 = []; l2 = []

question_vectors = []

ranks = []
for idx, question in enumerate(questions):
  temp = word_tokenize(question)
  question_vectors.append(temp)

  user = word_tokenize(x)

  # remove stop words from the string
  temp_set = {w for w in temp if not w in sw}
  user_set = {w for w in user if not w in sw}

  # form a set containing keywords of both strings
  rvector = temp_set.union(user_set)
  for w in rvector:
      if w in user_set:
          l1.append(1) # create a vector
      else:
          l1.append(0)
      if w in temp_set:
          l2.append(1)
      else:
          l2.append(0)
  c = 0

  # cosine formula
  for i in range(len(rvector)):
          c+= l1[i]*l2[i]
  cosine = c / float((sum(l1)*sum(l2))**0.5)
  print("similarity: ", cosine)
  ranks.append((idx, cosine))

ranks.sort(key=lambda y: y[1])
print(ranks)
print(answers[ranks[0][0]])
print(answers[ranks[1][0]])
