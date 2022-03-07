import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import spacy
nlp = spacy.load("en_core_web_md")

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import math

nltk.download('stopwords')
nltk.download('punkt')


def read_file(question):
    questions = [], []

    with open(question, 'r') as file:
        questions = file.readlines()

    return questions


sw = stopwords.words("english")


def find_similarity(questions, user):
    user_doc = nlp(user)

    ranks = []
    for idx, question in enumerate(questions):
        question_doc = nlp(question)
        similarity = user_doc.similarity(question_doc)
        ranks.append((idx, similarity))

    sorted_ranks = sorted(ranks, key=lambda x: x[1], reverse=True)
    return sorted_ranks

def answer(ranks):
    f_idx, s_idx = ranks[0][0], ranks[1][0]

    return f_idx


if __name__ == "__main__":
    questions = read_file("data/questions.txt")
    ranks = find_similarity(questions, "Can you tell me what an IEP is")
    answer(ranks)
