from bs4 import BeautifulSoup
import requests


class VSBattles():
    def __init__(self, name):
        self.url = "https://vsbattles.fandom.com/wiki/" + name
        self.soup = BeautifulSoup(requests.get(self.url).text, "lxml")

        self.tier = self.get_tier()
        self.name = self.get_name()
        self.origin = self.get_origin()
        self.gender = self.get_gender()
        self.age = self.get_age()
        self.classification = self.get_classification()

    def get_tier(self):
        html = self.soup.find(
            "a", text="Tier").find_parent().find_parent().text
        tier = html.replace("Tier: ", "")

        return tier

    def get_name(self):
        html = self.soup.find("b", text="Name:").find_parent().text
        name = html.replace("Name: ", "")

        return name

    def get_origin(self):
        html = self.soup.find("b", text="Origin:").find_parent().text
        origin = html.replace("Origin: ", "")

        return origin

    def get_gender(self):
        html = self.soup.find("b", text="Gender:").find_parent().text
        gender = html.replace("Gender: ", "")

        return gender

    def get_age(self):
        html = self.soup.find("b", text="Age:").find_parent().text
        age = html.replace("Age: ", "")

        return age

    def get_classification(self):
        html = self.soup.find("b", text="Classification:").find_parent().text
        classification = html.replace("Classification: ", "")

        return classification

    def bio(self):
        bio = [
            f"**Tier:** {self.tier}",
            f"**Origin:** {self.origin}",
            f"**Gender:** {self.gender}",
            f"**Age:** {self.age}",
            f"**Classification:** {self.classification}",
        ]

        return "".join(bio)

    def image(self):
        html = self.soup.find("div", class_="wds-tab__content wds-is-current")
        html = html.find("div", class_="floatright").a.img

        return html["src"]

    def summary(self):
        html = self.soup.find("span", class_="mw-headline", id="Summary")
        html = html.find_parent()

        summary = []
        while html.find_next_sibling().name == "p":
            if html.find_next_sibling().name == "p":
                summary.append(html.find_next_sibling().text)

            html = html.find_next_sibling()

        return "\n".join(summary)
