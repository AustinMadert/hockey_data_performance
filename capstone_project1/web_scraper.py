from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import random, time


client = MongoClient()
database = client['hockey_stats']
nhl_mongo_connect = database['nhl']
espn_mongo_connect = database['espn']


def scrape(url, stall, site='nhl'):
    
    try:
        website = requests.get(str(url))
    except:
        print("Requests error with url")
    
    with open('scrape_records.log', 'a+') as log:
        log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
        log.write('URL: {}, Status: {}\n'.format(url,website.status_code))


    if site == 'nhl':
        try:
            parsed_site = nhl_parser(website)
        except:
            print("Parse error with nhl.com url")
    else:
        try:
            parsed_site = espn_parser(website)
        except:
            print("Parse error with espn.com url")
    
    dictionary = {str(url): parsed_site}
    
    try:
        if site == 'nhl':
            store(dictionary, 'nhl')
        else:
            store(dictionary, 'espn')
    except:
        print("Store error with url")
    print("URL data successfully stored in database.")
    time.sleep(stall)
    pass

def nhl_parser(website):
    nhl_soup = BeautifulSoup(website.text, 'html.parser')
    nhl_tbodies = nhl_soup.find_all('tbody')
    parsed_site = [obj.find_all('td') for obj in nhl_tbodies]
    return parsed_site

def espn_parser(website):
    espn_soup = BeautifulSoup(website.text, 'html.parser')
    espn_tbodies = espn_soup.find_all('tbody', class_='Table2__tbody')
    parsed_site = [obj.find_all('td', class_='Table2__td') for obj in espn_tbodies]
    return parsed_site

def store(data, site):
    if site == 'nhl':
        nhl_mongo_connect.insert_one(data)
    else:
        espn_mongo_connect.insert_one(data)
    pass

if __name__ == __main__:
    rounds = {'1', '2', '3', '4', '5', '6', '7'}
    for i in rounds:
        scrape('http://www.nhl.com/ice/draftsearch.htm?year=&team=&position=&round=' + i, 20, 'nhl')
    
    teams = {'buf', 'car', 'mtl', 'ott', 'ari', 'det', 'van', 'chi', 'nyr', 'edm', 'nyi', 'dal',\
         'phi', 'fla', 'col', 'njd', 'cbj', 'lak', 'sjs', 'ana', 'min', 'stl', 'tor', 'wsh', 'bos',\
        'tbl', 'nsh', 'wpg', 'pit', 'cgy', 'vgk'}
    seasons = {'1', '2', '3'}
    years = {'2003', '2004', '2003', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', \
        '2013', '2014', '2015', '2016', '2017', '2018', '2019'}
    
    for i in teams:
        for k in years:
            for j in seasons:
                scrape('http://www.espn.com/nhl/team/schedule/_/name/{}/season/{}/seasontype/{}'.format(i,k,j),\
                    20, 'espn')