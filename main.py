import datetime
import time 
from plyer import notification
import requests
from bs4 import BeautifulSoup


def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="12.ico",
        timeout  = 6
    )

def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        myData=getData("https://www.worldometers.info/coronavirus/")
        soup = BeautifulSoup(myData, 'html.parser')
        covidtable=soup.find("table",attrs={"id":"main_table_countries_today"})
        body=covidtable.tbody.find("tr",attrs={"data-continent":"Asia"})
        l=[]
        for td in body.find_all("td"):
            l.append(td)

        ntitle="Cases of Covid in "+ l[1].get_text()+":\n"
        b="Total Cases: "+l[2].get_text() + "\n" +"New Cases: "+l[3].get_text()+"\n"+"Total Deaths: "+l[4].get_text()+"\n"+"New Deaths: "+l[5].get_text()+"\n"+"Active Cases: "+l[7].get_text()
        notify(ntitle,b)
        time.sleep(3600)