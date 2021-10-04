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
        self.answers = self.get_answers()

    def get_answers(self):
        numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]

        answers = self.incorrects + [self.correct]
        answers = random.sample(answers, len(answers))

        return dict(zip(numbers, answers))

    def format_answers(self):
        results = ""
        for answer in self.answers:
            results += f"{answer} . {self.answers[answer]} \n"

        return results
