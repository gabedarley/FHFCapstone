import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import math

nltk.download('stopwords')
nltk.download('punkt')


def read_file(answer, question):
    answers, questions = [], []

    with open(answer, 'r') as file:
        answers = file.readlines()

    with open(question, 'r') as file:
        questions = file.readlines()

    return answers, questions


sw = stopwords.words("english")


def find_similarity(questions, user):
    ranks = []

    # tokenize the user's question
    tokenized_user = word_tokenize(user)
    user_set = {w for w in tokenized_user if not w in sw}

    for idx, question in enumerate(questions):
        l1, l2 = [], []

        # tokenize the DB's question
        tokenized_question = word_tokenize(question)
        question_set = {w for w in tokenized_question if not w in sw}

        rvector = question_set.union(user_set)
        for w in rvector:
            if w in user_set:
                l1.append(1)
            else:
                l1.append(0)

            if w in question_set:
                l2.append(1)
            else:
                l2.append(0)

        c = 0
        # cosine formular
        for i in range(len(rvector)):
            c += l1[i]*l2[i]
        cosine = c / ((sum(l1)**0.5*(sum(l2))**0.5))

        # for each question, find its similarity to user's question
        ranks.append((idx, cosine))

    # sort the ranks
    ranks.sort(key=lambda y: y[1], reverse=True)
    print(ranks[0])
    print(ranks[1])
    return ranks


def answer(ranks, answers):
    f_idx, s_idx = ranks[0][0], ranks[1][0]

    print("The first answer is", answers[f_idx])
    print("The second answer is", answers[s_idx])

    return answers[f_idx]


if __name__ == "__main__":
    answers, questions = read_file("data/answers.txt", "data/questions.txt")
    ranks = find_similarity(questions, "Can you tell me what an IEP is")
    answer(ranks, answers)
