from flask import Flask
from flask import request
from chatbot import read_file, find_similarity, answer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

answers, questions = read_file("data/answers.txt", "data/questions.txt")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/answer", methods=['POST'])
def answer_endpoint():
    message = request.json['message']
    ranks = find_similarity(questions, message)
    return answer(ranks, answers)


if __name__ == '__main__':
    app.run(debug=True)
