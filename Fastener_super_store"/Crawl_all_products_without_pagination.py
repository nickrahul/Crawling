
import requests
from bs4 import BeautifulSoup as BS
# from amazon import crawl
import pandas as pd

cookies = {
    '_session_id': '35406923d6e0362313aa4bcb9e6b2961',
    '_gcl_au': '1.1.86785013.1714628360',
    '_ga_3PP2E7TRS2': 'GS1.1.1714659918.2.1.1714659947.31.0.0',
    '_ga': 'GA1.1.940562935.1714628360',
    'ps_rvm_67Sx': '%7B%22pssid%22%3A%224LVMA0XJeml3prLA-1714659936760%22%2C%22last-visit%22%3A%221714659945991%22%7D',
    '_gid': 'GA1.2.622510090.1714628361',
    '_drip_client_2464071': 'vid%253D8dadd2433d814b81ace74af1d22b15f5%2526pageViews%253D102%2526sessionPageCount%253D2%2526lastVisitedAt%253D1714659935908%2526weeklySessionCount%253D2%2526lastSessionAt%253D1714659923889',
    '_clck': 'cd0aay%7C2%7Cflf%7C0%7C1583',
    'SNS': '1',
    '_sn_m': '{"r":{"n":1,"r":"fastenersuperstore"}}',
    '_sn_a': '{"a":{"s":1714659911776,"e":1714659293316}}',
    '_sn_n': '{"a":{"i":"ea45c323-85e1-43c5-a543-ac0f61c2a7a7"}}',
    '_gat_UA-621140-1': '1',
    '_clsk': 'obpzj7%7C1714659939058%7C2%7C1%7Cw.clarity.ms%2Fcollect',
    '_uetsid': '534af2a0084611efa2974f8a07d0ccad',
    '_uetvid': '534afc80084611efab90f7dc1d3e26d2',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.fastenersuperstore.com/products/concrete-screws?pid=5984',
    'X-CSRF-Token': 'XK1AAjNjdemjqowS+d+l5G1PIqxrYNn4qOCdZIlOwlYIG1Dl7o8PBCWzXbeitCdvFuB9YgO2hhvQsjCut7bAtg==',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    # 'Cookie': '_session_id=35406923d6e0362313aa4bcb9e6b2961; _gcl_au=1.1.86785013.1714628360; _ga_3PP2E7TRS2=GS1.1.1714659918.2.1.1714659947.31.0.0; _ga=GA1.1.940562935.1714628360; ps_rvm_67Sx=%7B%22pssid%22%3A%224LVMA0XJeml3prLA-1714659936760%22%2C%22last-visit%22%3A%221714659945991%22%7D; _gid=GA1.2.622510090.1714628361; _drip_client_2464071=vid%253D8dadd2433d814b81ace74af1d22b15f5%2526pageViews%253D102%2526sessionPageCount%253D2%2526lastVisitedAt%253D1714659935908%2526weeklySessionCount%253D2%2526lastSessionAt%253D1714659923889; _clck=cd0aay%7C2%7Cflf%7C0%7C1583; SNS=1; _sn_m={"r":{"n":1,"r":"fastenersuperstore"}}; _sn_a={"a":{"s":1714659911776,"e":1714659293316}}; _sn_n={"a":{"i":"ea45c323-85e1-43c5-a543-ac0f61c2a7a7"}}; _gat_UA-621140-1=1; _clsk=obpzj7%7C1714659939058%7C2%7C1%7Cw.clarity.ms%2Fcollect; _uetsid=534af2a0084611efa2974f8a07d0ccad; _uetvid=534afc80084611efab90f7dc1d3e26d2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = {
    'subcategory': 'Concrete Screws',
    'pid': '17291',
    '_': '1714659947288',
}

dataa=[]


class Crawl:
    def __init__(self,url) -> None:
        response = requests.get(url)
        if response.status_code==200:
            soup=BS(response.content,"html.parser")
            self.get_links_from_main_page(soup)

    
    def get_links_from_main_page(self,soup):
        for i in soup.find("section","category_list inner_col").find("ul").find_all("li"):
            links=("https://www.fastenersuperstore.com"+i.find("a").get("href"))
            self.categories(links)
            break

    def categories(self,links):
        r=requests.get(links)
        soup=BS(r.content,"html.parser")
        for i in soup.find("section","category_list").find_all("ul"):
            for j in i.find_all("li"):
                link="https://www.fastenersuperstore.com"+(j.find("a").get("href"))
                # print(link)
                self.sub_category(link)

    def sub_category(self,link):
        r=requests.get(link)
        soup=BS(r.content,"html.parser")
        if soup.find("div","col-sm-5"):
            url="https://www.fastenersuperstore.com"+soup.find("div","col-sm-5").find("a").get("href")
        else:
            url=link
        a=url.split("/")
        if "products" in a:
            self.list_page(url)
        else:
            self.again_sub_category_page(url)

    def list_page(self,url):
        cr=Crawl_from_api(url)


    def again_sub_category_page(self,url):
        r=requests.get(url)
        soup=BS(r.content,"html.parser")
        for i in soup.find("section","category_list").find_all("ul"):
            for j in i.find_all("li"):
                link="https://www.fastenersuperstore.com"+(j.find("a").get("href"))
                if "products" in link:
                    self.list_page(link)
                else:
                    self.more_list_page(link)

    def more_list_page(self,link):
        r=requests.get(link)
        soup=BS(r.content,"html.parser")
        if soup.find("div","col-sm-5"):
            url="https://www.fastenersuperstore.com"+soup.find("div","col-sm-5").find("a").get("href")
            self.list_page(url)
    


class Crawl_from_api:
    def __init__(self,url) -> None:
        r=requests.get(url)
        soup=BS(r.content,"html.parser")
        sub_category=soup.find("div","searchparams").get("data-searchparams").replace('"',"").replace(":",",").replace("}","").split(",")[1]
        self.pid=soup.find("div","searchparams").get("data-searchparams").replace('"',"").replace(":",",").replace("}","").split(",")[-1]
        params['subcategory']=sub_category
        params['pid']=self.pid
        self.data_from_list_page()

    def data_from_list_page(self):
        response = requests.get('https://www.fastenersuperstore.com/products/filter', params=params, cookies=cookies, headers=headers)
        js=response.json()
        for i in js["products"]:
            part_no=(i[0])
            data=(i[-1])
            url="https://www.fastenersuperstore.com"+f"/products/{part_no}/{data}?pid={self.pid}"
            self.data_from_detail_page(url)
    
    def data_from_detail_page(self,url):
        r=requests.get(url,cookies=cookies,headers=headers,params=params)
        soup=BS(r.content,"html.parser")
        try:
            title=soup.find("section","product_page").find("h1").text
        except:
            title="Not available"

        try:
            product_details=[]
            for i in soup.find("div","box_row").find_all("span"):
                   product_details.append(i.text.replace("\n","").replace("                  ","").strip())
        except:
            product_details="Not available"

        try:
            dic={}
            for i in soup.find_all("div","box_row")[1:]:
                key=(i.find("span","col_box").text)
                value=(i.find("span","col_box big").text.replace("\n","").replace("            ",""))
                dic.update({key:value})
        except:
            dic="Not available"


        try:
            dic2={}
            for i in soup.find("div","right_common").find_all("li"):
                key=i.find("span","left").text
                value=i.find("span","right").text
                dic2.update({key:value})
        except:
            dic2="Not available"

        dataa.append({
            "TITLE":title,
            "PRODUCT_DETAILS":product_details,
            "PRICING_INFORMATION":dic,
            "PRODUCT_SPECS":dic2
        })
        print(dataa)


df=pd.DataFrame(dataa)
df.to_excel("flp.xlsx")


url='https://www.fastenersuperstore.com/'
crl=Crawl(url)
