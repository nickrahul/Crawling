import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.snapdeal.com/',
    'Connection': 'keep-alive',
    # 'Cookie': 'versn=v1; u=171583958465157978; sd.zone=NO_ZONE; _gcl_au=1.1.1512692356.1713593055; st=utm_source%3DSEO%7Cutm_content%3Dnull%7Cutm_medium%3Dnull%7Cutm_campaign%3Dnull%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; lt=utm_source%3DSEO%7Cutm_content%3Dnull%7Cutm_medium%3Dnull%7Cutm_campaign%3Dnull%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; s_pers=%20s_vnum%3D1716185058948%2526vn%253D2%7C1716185058948%3B%20gpv_pn%3DallProducts%253Ahttps%253A%252F%252Fwww.snapdeal.com%252Fproduct%252Fcampus-vacum-navy-running-shoes%252F5764608146007740659%7C1715841914132%3B%20s_invisit%3Dtrue%7C1715841914132%3B; xg="eyJ3YXAiOnsiYWUiOiIxIn0sIm1hcGkiOnsidHBmIjoiQTIifSwic2MiOnsicnRvbW9kZWwiOiJBIiwicGRkIjoibWwwIn0sInBzIjp7ImF0IjoibyIsImNiIjoiQiJ9LCJ1aWQiOnsiZ3VpZCI6IjZlYmM1NmYzLTA4YmYtNDQxMy04Y2Y1LTAyMDFjOTE5OTg5YyJ9fXx8MTcxNTg0MTM4NDY1NA=="; xc="eyJ3YXAiOnsiYWUiOiIxIn0sIm1hcGkiOnsidHBmIjoiQTIifSwic2MiOnsicnRvbW9kZWwiOiJBIiwicGRkIjoibWwwIn0sInBzIjp7ImF0IjoibyIsImNiIjoiQiJ9fQ=="; alps=akm; _sdDPPageId=1715840112837_4675_171583958465157978; isWebP=true; vt=utm_source%3DSEO%7Cutm_content%3Dnull%7Cutm_medium%3Dnull%7Cutm_campaign%3Dnull%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20s_ppv%3D18%3B; sdCPW=false; AWSALB=4tuO6uUlJEeVEQVzvoV5xN095FVJJOV7hz5oQF3XzLcom+XyemNoc5Ks2bzTqyj1WHpcwxino1swhr/yFluEhso13auPWDEXrJT7NHinCz3jkeqjH0WDy+d6N0eU; AWSALBCORS=4tuO6uUlJEeVEQVzvoV5xN095FVJJOV7hz5oQF3XzLcom+XyemNoc5Ks2bzTqyj1WHpcwxino1swhr/yFluEhso13auPWDEXrJT7NHinCz3jkeqjH0WDy+d6N0eU; SCOUTER=z6j4a71cka1ehm; JSESSIONID=21FF832145152D6EABA626CAA8B2B1FB; _fbp=fb.1.1715839636702.2043460883; hpcl=255; _uetsid=7978c3e0134a11ef9ac39de09ad2b806; _uetvid=d1fee3c0fedb11eea6cdcfece2f6b759; _sdRefPgCookie=%7B%22refPg%22%3A%22categoryListing%22%2C%22refPgId%22%3A%221715840112837_4675_171583958465157978%22%7D; _sdRefEvtCookie=%7B%22refEvt%22%3A%22eventLoggingLogging%22%2C%22refEvtId%22%3A%221715840114167_7486_171583958465157978%22%7D',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'sort': 'plrty',
}




class Crawl:
    def __init__(self,url) -> None:
        self.data=[]
        response = requests.get(url,params=params,headers=headers)
        if response.status_code==200:
            soup=BS(response.content,"html.parser")
            self.list_page(soup)
            df=pd.DataFrame(self.data)
            df.to_excel("snap.xlsx")


    def list_page(self,soup):
        l=[]
        for i in soup.find_all("div","product-tuple-description"):
            links=(i.find("a").get("href"))
            self.detail_page(links)
            
        
        value=20
        while True:
            url=f'https://www.snapdeal.com/acors/json/product/get/search/255/{value}/20?q=&sort=plrty&brandPageUrl=&keyword=&searchState=k3=true|k5=0|k6=0|k7=MChAKBoAAAAAAAAABAWAIAAAAOBaAAAAAAAAAQgAAkAARDk8AQAIICIAgAAAAAEiAAIBIgIAAAEAAIQAAAQARAAEkAI=|k8=0&pincode=&vc=&webpageName=categoryPage&campaignId=&brandName=&isMC=false&clickSrc=unknown&showAds=true&cartId=&page=cp'
            r=requests.get(url,headers=headers)
            soup=BS(r.content,"html.parser")
            if soup.find("div","product-tuple-description"):
                for i in soup.find_all("div","product-tuple-image"):
                    links=(i.find("a").get("href"))
                    self.detail_page(links)
            else:
                break
            value+=20

    def detail_page(self,links):
        d={}
        r=requests.get(links,headers=headers)
        soup=BS(r.content,"html.parser")
        try:
            title=soup.find("h1","pdp-e-i-head").text.strip()
        except:
            title=None
        
        try:
            rating=soup.find("span","avrg-rating").text.replace("(","").replace(")","")
        except:
            rating=None
        
        try:
            price=soup.find("span","pdp-final-price").text.replace("\xa0","")
        except:
            price=None

        try:
            sizes=[]
            for i in soup.find("div","attr-value-cont sqt-attr-val").find_all("div","pull-left"):
                sizes.append(i.text.strip())
            sizes=",".join()
        except:
            sizes=None

        d.update({"TITLE":title,"RATING":rating,"PRICE":price,"SIZES":sizes})
        self.data.append(d)
        print(len(self.data))



url='https://www.snapdeal.com/products/mens-footwear-sports-shoes'
crl=Crawl(url)
