import requests
import random
import json


class TriviaDB():
    def __init__(self):
        self.quiz = json.loads(requests.get(
            "https://opentdb.com/api.php?amount=1&category=31&difficulty=easy&type=multiple").text)
        self.question = self.quiz["results"][0]["question"]
        self.incorrects = self.quiz["results"][0]["incorrect_answers"]
        self.correct = self.quiz["results"][0]["correct_answer"]

    def get_answers(self):
        answers = self.incorrects + [self.correct]

        return random.sample(answers, len(answers))
