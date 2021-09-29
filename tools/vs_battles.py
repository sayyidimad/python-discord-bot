from bs4 import BeautifulSoup
import requests

class vs_battles():
    @staticmethod
    def character(name="Goku_Black"):
        html = requests.get(f'https://vsbattles.fandom.com/wiki/{name}').text
        soup = BeautifulSoup(html, "lxml")
        character = soup.find("div", class_="tabber wds-tabber")

        quote = character.find("div", class_="wds-tab__content wds-is-current").table.tbody.tr
        quote = quote.find_all("td")[1].i.text

        return quote