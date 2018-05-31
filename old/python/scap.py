import requests
from bs4 import BeautifulSoup
import geopy.distance
from pymongo import MongoClient
import time

client = MongoClient()
# specify url
url = 'http://www.seismo.ethz.ch/fr/earthquakes/switzerland/last-90-days/'

home_coords= (46.4886,6.73022)


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('tbody')

data=[]
rows = table.find_all('tr')
i = 0
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    position= (float(cols[4]),float(cols[5]))
    distance =geopy.distance.vincenty(home_coords, position)
    if (distance< 50):
        cols.append(distance)
        row_data={"date": cols[0],"magnitude":cols[1],"place":cols[2],"depth":cols[3],"lat":cols[4],"long":cols[5]}
        data.append(row_data)
    i +=1
    if ( i> 10):
        break




for event in data:
    cursor = message.find({"type": "earthquake","id":event['date']})
    if (cursor.count()== 0):
        id = event['date']
        new_message = {"id": id, "type": "earthquake", "time": time.time(), "last_showed": 0, "icon": "",
                   "content": event}


        print('insert')




