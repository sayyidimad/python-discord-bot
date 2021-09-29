from bs4 import BeautifulSoup
import requests

class vs_battles():
    soup = ""

    def __init__(self, name):
        vs_battles.soup = BeautifulSoup(requests.get(f'https://vsbattles.fandom.com/wiki/{name}').text, "lxml")

    def bio(self):
        character = vs_battles.soup.find("span", class_="mw-headline", id="Powers_and_Stats")
        character = character.find_parent()

        bio = []
        while character.find_next_sibling().name == "p":
            if character.find_next_sibling().b.text == "Powers and Abilities:":
                break

            if character.find_next_sibling().name == "p":
                bio.append(character.find_next_sibling().text)

            character = character.find_next_sibling()

        return "".join(bio)

    def summary(self):
        character = vs_battles.soup.find("span", class_="mw-headline", id="Summary")
        character = character.find_parent()

        summary = []
        while character.find_next_sibling().name == "p":
            if character.find_next_sibling().name == "p":
                summary.append(character.find_next_sibling().text)

            character = character.find_next_sibling()

        return "\n".join(summary)