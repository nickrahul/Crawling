import requests
from bs4 import BeautifulSoup as BS
import pandas as pd


cookies = {
    '_ga': 'GA1.2.745286321.1711177725',
    '_ga_NTHR9DD8FN': 'GS1.2.1714540871.6.0.1714540871.0.0.0',
    'ASP.NET_SessionId': '50syqxk1ziyowoktybm4tvzq',
    'AuthToken': '74e97a52-7b75-424f-8c5c-2d959a93b365',
    'ARRAffinity': '498f1c8e0836506e62b6c050f04a3c2889fb20f3373dc59f688f2ea29957043d',
    '_gid': 'GA1.2.1301272507.1714464350',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json; charset=utf-8',
    'Ticket': '74e97a52-7b75-424f-8c5c-2d959a93b365',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'http://yellowpages.in',
    'Connection': 'keep-alive',
    'Referer': 'http://yellowpages.in/hyderabad/apparels-and-accessories/110497301',
    # 'Cookie': '_ga=GA1.2.745286321.1711177725; _ga_NTHR9DD8FN=GS1.2.1714540871.6.0.1714540871.0.0.0; ASP.NET_SessionId=50syqxk1ziyowoktybm4tvzq; AuthToken=74e97a52-7b75-424f-8c5c-2d959a93b365; ARRAffinity=498f1c8e0836506e62b6c050f04a3c2889fb20f3373dc59f688f2ea29957043d; _gid=GA1.2.1301272507.1714464350',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

json_data = {
    'uId': '110497301',
    'loc': 'hyderabad',
    'eInd': 25,
    'filterParams': [],
    'sort': 'Popular',
}

response = requests.post('http://yellowpages.in/helper.aspx/GetBusinessByCatFilter',cookies=cookies,headers=headers,json=json_data,)
js=response.json()

start=int(js["d"][1])-1
end=int(js["d"][2])

l=[]

def detail_page(link):
    r=requests.get(link)
    soup=BS(r.content,"html.parser")
    try:
        title=soup.find("div","businessTitleInfo").find("h1").text
    except:
        title="Not available"

    try:
        address=soup.find("address","businessAddress").text
    except:
        address="Not available"

    try:
        phone_no=soup.find("div","businessContact").find("a").text
    except:
        phone_no="Not available"

    try:
        timings={}
        for i in soup.find("ul",{"id":"MainContent_ulTimings"}).find_all("li"):
            days=i.find("span","dayDisplay")
            timing=i.find("span","timeDisplay")
            timings.update({days.text:timing.text})
    except:
        timings="Not available"

    l.append({
        "TITLE":title,
        "ADDRESS":address,
        "PHONE_NO":phone_no,
        "TIMINGS":timings
    })



try:
    while True:
        response = requests.post('http://yellowpages.in/helper.aspx/GetBusinessByCatFilter',cookies=cookies,headers=headers,json=json_data,)
        js=response.json()
        data=(js["d"][0])
        soup=BS(data,"html.parser")
        for i in soup.find_all("div","eachPopular"):
            link=("http://yellowpages.in"+i.find("a").get("href"))
            detail_page(link)
        print(len(l))
        json_data["eInd"]+=start
        if json_data["eInd"]==end:
            break
except:
    None
