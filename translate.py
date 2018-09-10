import re
import json
import urllib3


class Translate(object):

    def __init__(self, url="http://127.0.0.1:8080"):
        self.url = url

    def count_words(self, text):
        dict_words = {}
        text = re.sub('[^A-Za-z\']', ' ', text)
        words = text.lower().split()
        for word in words:
            if len(word) > 2:
                if word in dict_words:
                    dict_words[word][0] += 1
                else:
                    dict_words[word] = [1, ""]

        return dict_words

    def translate_words(self, dict_words):
        list_of_words = []

        for word in dict_words:
            list_of_words.append(word)

        to_translate = json.dumps({"words": list_of_words})

        http = urllib3.PoolManager()
        get_translate = http.request('POST', self.url,
                                     headers={'Content-Type': 'application/json'},
                                     body=to_translate)
        data = get_translate.data.decode("utf-8")

        translates = json.loads(data)

        for word in dict_words:
            dict_words[word][1] = translates[word]

        return dict_words

    def sort_words(self, dict_words):
        dict_words = sorted(dict_words.items(), key=lambda x: x[1], reverse=True)

        return dict_words
