from flask import Flask
from flask import request
from chatbot import read_file, find_similarity, answer
from flask_cors import CORS
from filewriter import newRead, findAnswer

app = Flask(__name__)
CORS(app)

newRead()
print("Successful read")
questions = read_file("data/questions.txt")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/answer", methods=['POST'])
def answer_endpoint():
    message = request.json['message']
    ranks = find_similarity(questions, message)
    a_index = answer(ranks)
    return findAnswer(a_index)


if __name__ == '__main__':
    app.run(debug=True)
