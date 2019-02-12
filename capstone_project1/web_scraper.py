from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import random, time

def scrape(urls, stall):
    for ind, lst in enumerate(urls):
        try:
            website = requests.get(str(ind))
        except:
            print("Requests error with url #" + str(ind))
        try:
            data = parser(website)
        except:
            print("Parse error with url " + str(ind))
        try:
            store(data)
        except:
            print("Store error with url " + str(ind))
        print("URL data successfully stored in database.")
        time.sleep(stall)
    pass

def parser(website):
    soup = BeautifulSoup(website.text, 'html.parser')

    return data

def store():

    #mongo_connect.insert_one()
    pass