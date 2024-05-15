import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import time


cookies = {
    '_ga': 'GA1.2.745286321.1711177725',
    '_ga_NTHR9DD8FN': 'GS1.2.1715665247.13.1.1715666020.0.0.0',
    'ASP.NET_SessionId': '50syqxk1ziyowoktybm4tvzq',
    'AuthToken': '74e97a52-7b75-424f-8c5c-2d959a93b365',
    'ARRAffinity': 'a40489a302b90bd3d9f4a6c226a89574de774279522c34e2e10a14706de0dfba',
    '_gid': 'GA1.2.583611969.1715665247',
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
    # 'Cookie': '_ga=GA1.2.745286321.1711177725; _ga_NTHR9DD8FN=GS1.2.1715665247.13.1.1715666020.0.0.0; ASP.NET_SessionId=50syqxk1ziyowoktybm4tvzq; AuthToken=74e97a52-7b75-424f-8c5c-2d959a93b365; ARRAffinity=a40489a302b90bd3d9f4a6c226a89574de774279522c34e2e10a14706de0dfba; _gid=GA1.2.583611969.1715665247',
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


class Crawl:
    def __init__(self,url) -> None:
        self.data=[]
        r=requests.get(url)
        if r.status_code==200:
            soup=BS(r.content,"html.parser")
            self.main_page(soup)
            df=pd.DataFrame(self.data)
            df.to_excel("ajio.xlsx",index=False)

    def main_page(self,soup):
        for i in soup.find("ul",id="ulCats").find_all("a"):
            link="http://yellowpages.in"+(i.get("href"))
            name=i.find("div","eachCategoryname").text
            time.sleep(3)
            self.list_page(link,name)


    
    def list_page(self,link,name):
        lis=[]
        a=link.split("/")
        json_data['uId']=a[-1]
        r=requests.get(link)
        soup=BS(r.content,"html.parser")
        json_data['eInd']=25
        print(json_data)
        for i in soup.find("ul",id="MainContent_ulFList").find_all("li"):
            if i.find("div","popularTitleTextBlock"):
                links="http://yellowpages.in"+(i.find("a").get("href"))
                d=self.detail_page(links)
                lis.append(d)
                print(len(lis))
        try:
            while True:
                json_data["eInd"]+=25
                headers["Referer"]=link
                print(json_data)
                response = requests.post('http://yellowpages.in/helper.aspx/GetBusinessByCatFilter',cookies=cookies,headers=headers,json=json_data)
                js=response.json()
                a=js["d"][0]
                so=BS(a,"html.parser")
                for k in so.find_all("li"):
                    if k.find("div","popularTitleTextBlock"):
                        links="http://yellowpages.in"+(k.find("div","popularTitleTextBlock").find("a").get("href"))
                        d=self.detail_page(links)
                        lis.append(d)
                        print(len(lis))
                if int(js["d"][-1])==len(lis):
                    break
        except:
            None
        self.data.extend(lis)
        # d={name:lis}
        # self.data.append(d)

        


    def detail_page(self,link):
        di={}
        r=requests.get(link)
        soup=BS(r.content,"html.parser")
        try:
            title=soup.find("h1",id="MainContent_h1").text.strip()
        except:
            title=None

        try:
            address=soup.find("address","businessAddress").text
        except:
            address=None

        try:
            phone_no=soup.find("a",class_="businessContactNumber").text
        except:
            phone_no=None
        
        di.update({"TITLE":title,"ADDRESS":address,"PHONE_N0":phone_no})
        return di

url="http://yellowpages.in/"
crl=Crawl(url)
