from bs4 import BeautifulSoup
import requests


class Scrape(object):
    
    def __init__(self, sites=[], mongo_db=None, stall=15):
        self._sites = sites
        self._mongo_db = mongo_db
        self._stall = stall

    