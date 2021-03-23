import requests
from bs4 import BeautifulSoup
import time

url = "https://xkcd.com/"


def comicscraper():
    mycomics = ""
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    comicdiv = soup.find("div", {"id": "comic"})
    imagelink = "https://" + comicdiv.img["src"].replace("//", "")
    mycomics += imagelink
    # print(mycomics)
    with open("xkcd_comics.txt", mode="a") as schrijven:
        schrijven.write(mycomics + "\n")
        print("Succes")


def prevbutton():
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    prevdiv = soup.find('a', href=True, accesskey=True)
    link = prevdiv["href"].replace("/", "")
    prevurl = "https://xkcd.com/" + link
    return prevurl


while True:
    comicscraper()
    url = prevbutton()
    time.sleep(3)
