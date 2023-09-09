import random
#import requests
import json
from datetime import datetime

webhook = "https://discordapp.com/api/webhooks/994500147444711484/OyxX_dvRPdGxfkaJVi5WWgfmU5QdAKk8ZOH2b0AeWXMA9IqXNFsEctqz77VNxPlh5wIk"


def getRandomItem(no_of_items):
    with open("./N2_processed.list", 'r') as raw_list_file:
        print(json.load(raw_list_file)[2])
   
def send_to_bot(contents):
    data={"content": contents}
    print(contents)
    #requests.post(webhook, json=data)

def format_jlpt_content(arr):
    return (
        f'{{\n'
        f'  "number": "{replaceEmpty(arr[0])}",\n'
        f'  "romaji_word": "{replaceEmpty(arr[1])}",\n'
        f'  "kanji_word": "{replaceEmpty(arr[2])}",\n'
        f'  "word_type": "{replaceEmpty(arr[3])}",\n'
        f'  "english_meaning": "{replaceEmpty(arr[4])}"\n'
        f'}},'
    )

def replaceEmpty(item):
    if item == '':
        return "-"
    return item

with open("./N2_raw_pipe.list", 'r') as raw_list_file:
    for line in raw_list_file:
        # print(line.strip("\n"))
        item_array = line.strip("\n").split('|')
        print(format_jlpt_content(item_array))

        