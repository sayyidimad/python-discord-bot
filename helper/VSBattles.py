from bs4 import BeautifulSoup
import requests

class VSBattles():
    soup = ""

    def __init__(self, name):
        VSBattles.soup = BeautifulSoup(requests.get(f'https://vsbattles.fandom.com/wiki/{name}').text, "lxml")

    def bio(self):
        html = VSBattles.soup.find("span", class_="mw-headline", id="Powers_and_Stats")
        html = html.find_parent()

        bio = []
        while html.find_next_sibling().name == "p":
            if html.find_next_sibling().b.text == "Powers and Abilities:":
                break

            if html.find_next_sibling().name == "p":
                bio.append("> " + html.find_next_sibling().text)

            html = html.find_next_sibling()

        return "".join(bio)

    def image(self):
        html = VSBattles.soup.find("div", class_="wds-tab__content wds-is-current")
        html = html.find("div", class_="floatright").a.img

        return html["src"]

    def summary(self):
        html = VSBattles.soup.find("span", class_="mw-headline", id="Summary")
        html = html.find_parent()

        summary = []
        while html.find_next_sibling().name == "p":
            if html.find_next_sibling().name == "p":
                summary.append(html.find_next_sibling().text)

            html = html.find_next_sibling()

        return "```" + "\n".join(summary) + "```"