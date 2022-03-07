import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

def newRead():
    scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("testkey.json", scopes)
    file = gspread.authorize(credentials) # authenticate the JSON key with gspread
    sheet = file.open("QA Window") #open sheet
    sheet = sheet.sheet1

    f = open('data/questions.txt', 'w+')

    questions_col = sheet.col_values(1)
    #print(questions_col)

    for i in range(1, len(questions_col)):
        f.write(questions_col[i] + "\n")

    f.close()

def findAnswer(a_index):
    scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("testkey.json", scopes)
    file = gspread.authorize(credentials) # authenticate the JSON key with gspread
    sheet = file.open("QA Window") #open sheet
    sheet = sheet.sheet1

    answers_col = sheet.col_values(2)

    return answers_col[a_index + 1]
