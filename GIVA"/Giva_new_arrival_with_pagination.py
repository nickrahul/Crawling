import requests
from bs4 import BeautifulSoup as BS
import time
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.giva.co/collections/new-collection',
    'Alt-Used': 'www.giva.co',
    'Connection': 'keep-alive',
    # 'Cookie': 'keep_alive=527da320-4747-455b-9e03-a33cc1167ef9; secure_customer_sig=; localization=IN; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D; _tracking_consent=%7B%22v%22%3A%222.1%22%2C%22reg%22%3A%22%22%2C%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%2C%22m%22%3A%22%22%7D%7D%2C%22region%22%3A%22INDL%22%7D; _shopify_y=c3aaa20c-3969-4add-a761-9a9d0e938298; _shopify_s=efab0ea6-6d46-43cc-b84e-af35361d729a; _orig_referrer=; _landing_page=%2Fcollections%2Fnew-collection; _shopify_sa_t=2024-05-15T10%3A03%3A56.400Z; _shopify_sa_p=; _gcl_au=1.1.2053887964.1715767431; _ga_34LM183QM4=GS1.1.1715767432.1.1.1715767441.51.0.0; _ga=GA1.1.283305212.1715767433; _fbp=fb.1.1715767433296.751998333; _clck=11lwg51%7C2%7Cfls%7C0%7C1596; _ga_F1NJ1E2HJ2=GS1.1.1715767433.1.1.1715767437.0.0.0; swym-session-id="xowex1ch2wegfiu7mo62negft5h4s04ncvuy48y6py5xq59cta1zw18ikq9eyq7m"; swym-pid="ww6VoVDv1y3rHsp9RKpg7dkHxh+vDHrWI01W1cZ1on4="; _clsk=1iy87ah%7C1715767438583%7C2%7C1%7Cs.clarity.ms%2Fcollect; trackingId3=lw7nmpdw41kxrwqh0p4; visitId3=lw7nmpe3ad6te815kyi; last_referrer3=direct; _cnt_geo_country=India; _cnt_event_user_id=zv78e56dujkaqlhhv3tjm; _cnt_forms_status=%7B%7D; _cnt_cart_json=%7B%7D; _cnt_first_visit_time=1715767439.239; _cnt_last_visit_time=1715767439.239; _cnt_current_visit_time=1715767439.239; _cnt_num_of_vists=1; swym-o_s=true; swym-swymRegid="dE6svOY-RIRrHmWHJlxLKr4BkP1WN1o3FlgUHAkJkrVvl8ZN2hanpjliQbb2sQsFL0PsU1VmKJinHwiZOuZ3X6A010udwWqpu0HdC6yXR0qyEdB1BY76_I0QMlfF3zMr01Pw_X_mPI8ECCOuOt9YYxqU3vbDMA8AC29Evgblb2k"; swym-email=null; swym-cu_ct=undefined; _uetsid=73dd2ca012a211ef99b1c99a23585126; _uetvid=73dd880012a211ef8d1fa5f7233ca71c; _cnt_is_custom=false; cjConsent=MHxOfDB8Tnww; cjUser=12c9d75e-376f-4cb0-852b-7a27b8a37e1e; _cnt_user_push_consent=false',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


class Crawl:
    def __init__(self,url) -> None:
        self.data=[]
        response = requests.get(url, headers=headers)
        if response.status_code==200:
            soup=BS(response.content,"html.parser")
            self.list_page(soup)
            df=pd.DataFrame(self.data)
            df.to_excel("GIVA.xlsx",index=False)


    def list_page(self,soup):
        l=[]
        for i in range(1,13):
            r=requests.get(f"https://www.giva.co/collections/new-collection?page={i}")
            soup=BS(r.content,"html.parser")
            for i in soup.find_all("a","full-unstyled-link"):
                if "https://www.giva.co"+i.get("href") not in l:
                    l.append("https://www.giva.co"+i.get("href"))
        for link in l:
            self.detail_page(link)
            print(len(self.data))
            


    
    def detail_page(self,link):
        d1={}
        r=requests.get(link,headers=headers)
        soup=BS(r.content,"html.parser")
        try:
            name=soup.find("h2","main__title").text
        except:
            name=None
        
        try:
            current_price=soup.find("span","price-item price-item--sale price-item--last").text.strip()
        except:
            current_price=None
        
        try:
            mrp=soup.find("s",id="gold_card_regular_price").next.next.next.next.next.next.strip()
        except:
            mrp=None

        try:
            images=[]
            for i in soup.find("ul",id="Slider-Thumbnails-template--16317651517602__main").find_all("button"):
                images.append(i.find("img").get("src").replace("//",""))
            images=",".join(images)
        except:
            images=None

        try:
            d={}
            key=soup.find("div","product__description rte").find("span").find("strong").text.replace(":","")
            value=soup.find("div","product__description rte").find("span").find("strong").next.next.next
            d.update({key:value})
        except:
            d=None
        
        try:
            key2=soup.find("div","product__description rte").find("span").find_all("strong")[1].text.replace(":","")
            value2=soup.find("div","product__description rte").find("span").find_all("strong")[1].next.next.next
            d.update({key2:value2})
        except:
            d=None
        d1.update({"NAME":name,"CURRENT_PRICE":current_price,"MRP":mrp,"IMAGES":images})
        try:
            d1.update(d)
        except:
            None
        self.data.append(d1)
        


url='https://www.giva.co/collections/new-collection'
crl=Crawl(url)
