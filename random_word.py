import random
import requests
import json
from datetime import datetime

webhook = "https://discordapp.com/api/webhooks/994500147444711484/OyxX_dvRPdGxfkaJVi5WWgfmU5QdAKk8ZOH2b0AeWXMA9IqXNFsEctqz77VNxPlh5wIk"

def display_info(word_info):
    return (
        f'{word_info["kanji_word"]}({word_info["romaji_word"]}) => {word_info["english_meaning"]}'
    )

def getRandomItem(no_of_items):
    contents = ""

    rand_numbers = sorted(random.choices(range(4960), k=no_of_items), reverse=True)

    raw_file = open("./N2_processed.json", "r")
    json_file = json.loads(raw_file.read())

    index = 0
    rand_no = rand_numbers.pop()
    for i in json_file["words"]:
        if (i["number"] == str(rand_no)):
            contents += display_info(i) +"\n"
            if (rand_numbers):
                rand_no = rand_numbers.pop()

        index += 1

    return contents

def formatContent(content):
    formattedContent = """
        <html>
            <h2>割れる</h2>
        </html>
    """
    return formattedContent


def send_to_bot(contents):
    data={"content": contents}
    print(contents)
    requests.post(webhook, json=data)

send_to_bot(getRandomItem(5))