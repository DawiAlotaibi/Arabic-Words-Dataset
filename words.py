import requests
from bs4 import BeautifulSoup
import urllib3
import json

word_dict = ""
letter_dict = {}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
letters = ["alf", "hlf", "aaa", "eee", "hmz", "baa", "taa", "tah", "tha", "jim", "7aa", "kha", "dal", "thl", "raa",
           "zen", "sin", "shn", "sad", "dad", "6aa", "zaa", "3in", "ghn", "faa", "gaf", "kaf", "lam", "mim", "non",
           "haa", "waw", "waa", "yaa", "yea", "aae"]
url = "https://kalimmat.com/starts-with/"  # If you want to get words that start-with a specific letter.
# url = "https://kalimmat.com/ends-with/"  # If you want to get words that ends-with a specific letter.

for page in letters:
    try:
        kalmat = ""
        # response = requests.get(url + page, verify=False) # if you want only words from القاموس الشامل ( official dictionary)
        response = requests.get(url + page + "/1/1/2/", verify=False)  # if you want all common words
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        body = soup.findAll("div", class_="wordlist")

        for bodytext in body:
            if kalmat == "":
                kalmat = bodytext.text.strip()
            else:
                kalmat = kalmat + "\n" + bodytext.text.strip()
        words = kalmat.split("\n")
        words_sorted = sorted(words, key=len)

        cleaned_words = [word.replace(' ', '').replace(',', '').replace('.', '').replace('،', '') for word in
                         words_sorted]
        word_dict = {}
        for word in cleaned_words:
            word_len = len(word)
            if word_len == 0:
                continue
            if word_len not in word_dict:
                word_dict[word_len] = []
            word_dict[word_len].append(word)
        if page not in letter_dict:
            letter_dict[page] = {}
        letter_dict[page] = word_dict
    except requests.exceptions.HTTPError as err:
        # handle the error in some way, for example by logging it
        print(f"Error occurred: {err}")

json_data = json.dumps(letter_dict, ensure_ascii=False)
with open("startWithWords.json", "w", encoding="utf-8") as f:  # if you write in starts with.
# with open("endsWithWords.json", "w", encoding="utf-8") as f: # if you write in ends with.
    f.write(json_data)

print("Data written to file.")
