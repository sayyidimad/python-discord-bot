import requests
import json

class kanji():
    @staticmethod
    def search(word="see"):
        '''
        Fungsi untuk menterjemahkan kata dari bahasa Inggris menjadi Jepang dengan KanjiAlive API.
        
        Parameters
        ----------
        word: str, optional
            kata yang akan diterjemahkan ke dalam Kanji Jepang
        '''
        url = "https://kanjialive-api.p.rapidapi.com/api/public/search/advanced/"
        querystring = {"rem":word}
        headers = {
            'x-rapidapi-host': "kanjialive-api.p.rapidapi.com",
            'x-rapidapi-key': "cffe543a60msh7a6d9f78131a3a7p17436cjsnbc606a064d5f"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        json_data = json.loads(response.text)
        kanji = json_data[0]["kanji"]["character"]

        return kanji
