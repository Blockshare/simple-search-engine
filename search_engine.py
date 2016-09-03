# Loading Developer Libraries
import webhose
import requests
import os
import json
from flask import Flask, request

app = Flask(__name__)

# Loading Developer Key for Webhose

api_key = os.environ.get('KEY')
webhose.config(token=api_key)


def search_engine():

    search_input = input("Enter what you are searching for:\n")
    num_searches = input("How many search results would you like:\n")
    response = requests.get("https://webhose.io/search?token="+api_key+"&format=json&q=" \
                          + search_input)

    query = response.json()
    for i in range(0, int(num_searches)):
        params = {
            'site': query['posts'][i]['thread']['site_full'],
            'text': query['posts'][i]['text'],
            'title': query['posts'][i]['thread']['title'],
            'author': query['posts'][i]['author']
        }

        print(json.dumps(params, indent=2))

if __name__=='__main__':
    search_engine()
