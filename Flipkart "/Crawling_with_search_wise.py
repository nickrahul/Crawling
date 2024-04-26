
from bs4 import BeautifulSoup as BS

import requests
import pandas as pd
import time

cookies = {
    'T': 'clukuwo862mut1pdy352jcejb-BR1712212152486',
    'SN': 'VI37202652387A4B718D96FD17EE39F0E8.TOK871BC36414784F9CAF9D0822082518F1.1714034496.LO',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MTUyMzM5NDIsImlhdCI6MTcxMzUwNTk0MiwiaXNzIjoia2V2bGFyIiwianRpIjoiNDI2MGI5MDItYTgxMy00MDZiLWI5MTUtNDEwNzZhZTc2NDAxIiwidHlwZSI6IkFUIiwiZElkIjoiY2x1a3V3bzg2Mm11dDFwZHkzNTJqY2VqYi1CUjE3MTIyMTIxNTI0ODYiLCJrZXZJZCI6IlZJMzcyMDI2NTIzODdBNEI3MThEOTZGRDE3RUUzOUYwRTgiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.4dkDQpmJweXZvgKNcXa5a4lJCz_5PfB3cOJnp5KthMI',
    'K-ACTION': 'null',
    'ud': '6.TgT7YT6xQBy0GgnAGjqTbSn46hnU2pBg3Xd4bdV6xmGjk0tCnXYvkcgEceOIyrc_VpKNbz6GqponQB7xyI4GXtDlhbxgZICPzU9A48aWfUAq9SDt1bcqusIhV5dj2ME7EO3aiMKZ0VcvdpmfY2sEKw',
    'vh': '955',
    'vw': '1294',
    'dpr': '0.967741935483871',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19839%7CMCMID%7C00965089183736542750179575155903326637%7CMCAAMLH-1714373085%7C12%7CMCAAMB-1714629203%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1714031603s%7CNONE%7CMCAID%7CNONE',
    'rt': 'null',
    'vd': 'VI37202652387A4B718D96FD17EE39F0E8-1713505942932-17.1714034493.1714034412.155244381',
    '_pxvid': 'a83cab1c-f24c-11ee-9e01-a73a8dd08a0d',
    'S': 'd1t15cz8/ERBaPz8GXBguZT8RR2CBnP6gsuqOcVJ4SS63kaMzSKQ+fVGEhndL0uKbEiu00KeodsFUP30SZhFmvNHlNg==',
    'pxcts': '8abcc49b-ff53-11ee-8709-fc05767f0932',
    's_sq': 'flipkart-prd%3D%2526pid%253DHomePage%2526pidt%253D1%2526oid%253DSearch%252520Icon%2526oidt%253D3%2526ot%253DSUBMIT',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'fonts-loaded': 'en_loaded',
    'isH2EnabledBandwidth': 'true',
    'h2NetworkBandwidth': '9',
    '_px3': 'a0d6f91a93c2d5a5b7d74928e99fd4977dcdab56a5711a2bbc383ddbe3c45325:uCS9TZW6p9rnCsijxr9LSV5tqG2GCmBH831g2vuEipVfpIKitrU7W3SuCVKyQUU93imEQrmKjHNVdn2pXhfYqQ==:1000:oB5hfz4OpqyaUfhfo3r//YP86Hx2A0iaYpIvByhN2g22Hm3R1NDKCGfX4SaSUTa0yHtFTfNXabeSzESbu+sGVzN7p9CEhKm3EeFVCt9q8jClCpfnYnF5SwZtQ82nWAJdBClhJO+waOGuuQwKn4RfoH1MKUpHOv72/8FSrFvMkYnRGR/R6+17CamvH2SmIOa5NEQs5YsZWgmsAmeoEa2Tow+8TdtZ87s4uy+ssEw+Sf4=',
    'gpv_pn': 'HomePage',
    'gpv_pn_t': 'FLIPKART%3AHomePage',
    'qH': '0b3f45b266a97d70',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=clukuwo862mut1pdy352jcejb-BR1712212152486; SN=VI37202652387A4B718D96FD17EE39F0E8.TOK871BC36414784F9CAF9D0822082518F1.1714034496.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MTUyMzM5NDIsImlhdCI6MTcxMzUwNTk0MiwiaXNzIjoia2V2bGFyIiwianRpIjoiNDI2MGI5MDItYTgxMy00MDZiLWI5MTUtNDEwNzZhZTc2NDAxIiwidHlwZSI6IkFUIiwiZElkIjoiY2x1a3V3bzg2Mm11dDFwZHkzNTJqY2VqYi1CUjE3MTIyMTIxNTI0ODYiLCJrZXZJZCI6IlZJMzcyMDI2NTIzODdBNEI3MThEOTZGRDE3RUUzOUYwRTgiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.4dkDQpmJweXZvgKNcXa5a4lJCz_5PfB3cOJnp5KthMI; K-ACTION=null; ud=6.TgT7YT6xQBy0GgnAGjqTbSn46hnU2pBg3Xd4bdV6xmGjk0tCnXYvkcgEceOIyrc_VpKNbz6GqponQB7xyI4GXtDlhbxgZICPzU9A48aWfUAq9SDt1bcqusIhV5dj2ME7EO3aiMKZ0VcvdpmfY2sEKw; vh=955; vw=1294; dpr=0.967741935483871; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19839%7CMCMID%7C00965089183736542750179575155903326637%7CMCAAMLH-1714373085%7C12%7CMCAAMB-1714629203%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1714031603s%7CNONE%7CMCAID%7CNONE; rt=null; vd=VI37202652387A4B718D96FD17EE39F0E8-1713505942932-17.1714034493.1714034412.155244381; _pxvid=a83cab1c-f24c-11ee-9e01-a73a8dd08a0d; S=d1t15cz8/ERBaPz8GXBguZT8RR2CBnP6gsuqOcVJ4SS63kaMzSKQ+fVGEhndL0uKbEiu00KeodsFUP30SZhFmvNHlNg==; pxcts=8abcc49b-ff53-11ee-8709-fc05767f0932; s_sq=flipkart-prd%3D%2526pid%253DHomePage%2526pidt%253D1%2526oid%253DSearch%252520Icon%2526oidt%253D3%2526ot%253DSUBMIT; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; fonts-loaded=en_loaded; isH2EnabledBandwidth=true; h2NetworkBandwidth=9; _px3=a0d6f91a93c2d5a5b7d74928e99fd4977dcdab56a5711a2bbc383ddbe3c45325:uCS9TZW6p9rnCsijxr9LSV5tqG2GCmBH831g2vuEipVfpIKitrU7W3SuCVKyQUU93imEQrmKjHNVdn2pXhfYqQ==:1000:oB5hfz4OpqyaUfhfo3r//YP86Hx2A0iaYpIvByhN2g22Hm3R1NDKCGfX4SaSUTa0yHtFTfNXabeSzESbu+sGVzN7p9CEhKm3EeFVCt9q8jClCpfnYnF5SwZtQ82nWAJdBClhJO+waOGuuQwKn4RfoH1MKUpHOv72/8FSrFvMkYnRGR/R6+17CamvH2SmIOa5NEQs5YsZWgmsAmeoEa2Tow+8TdtZ87s4uy+ssEw+Sf4=; gpv_pn=HomePage; gpv_pn_t=FLIPKART%3AHomePage; qH=0b3f45b266a97d70',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}


class Crawl:
    def __init__ (self,li) -> None:
        for i in li:
            url=f"https://www.flipkart.com/search?q={i}"
            response = requests.get(url, cookies=cookies, headers=headers,timeout=5)
            soup=BS(response.content,"html.parser")
            if soup.find("div","tUxRFH"):
                self.hl=hlay()
                self.hl.Hlayout(url)

            elif soup.find("div","slAVV4"):
                self.v2=vlay2()
                self.v2.Vlayout2(url)

            elif soup.find("div","_1sdMkc LFEi7Z"):
                self.v1=vlay()
                self.v1.Vlayout(url)
            
            else:
                print("Search value incorrect")

   
class hlay:
    def Hlayout(self,url):
        self.data=[]
        a=url
        while True:
            r=requests.get(a,cookies=cookies, headers=headers,timeout=5)
            soup=BS(r.content,"html.parser")
            for i in soup.find_all("div","tUxRFH"):
                link=("https://www.flipkart.com"+i.find("a").get("href"))
                self.detail_page(link)
            
            if soup.find("nav","WSL9JP").find_all("a")[-1].text=="Next":
                a="https://www.flipkart.com"+soup.find("nav","WSL9JP").find_all("a")[-1].get("href")
            else:
                break
        df=pd.DataFrame(self.data)
        df.to_excel("flip.xlsx")


    def detail_page(self,link):
        r=requests.get(link,cookies=cookies,headers=headers,timeout=5)
        soup=BS(r.content,"html.parser")
        try:
            title=soup.find("h1","_6EBuvT").text
        except:
            title="Not available"

        try:
            rating=soup.find("div","XQDdHH").text
        except:
            rating="Not available"

        try:
            price=soup.find("div","Nx9bqj CxhGGd").text
        except:
            price="Not available"
        
        try:
            discount=soup.find("div","UkUFwK WW8yVX").text
        except:
            discount="Not available"
        
        try:
            variant=[]
            for i in soup.find("div","OYP50x").find_all("div","_3Rka5k col col-6-12")[1]:
                for j in (i.find_all("a")):
                    variant.append(j.text)
        except:
            variant="Not available"

        try:
            images=[]
            for j in soup.find("div","_0J1TKd").find("ul","ZqtVYK").find_all("li"):
                images.append(j.find("img").get("src"))
        except:
            images="Not available"

        self.data.append({
            "TITLE":title,
            "RATING":rating,
            "PRICE":price,
            "DISCOUNT":discount,
            "STORAGE_VARIANT":variant,
            "IMAGES_LINK":images
        })
        print(link)
        print(len(self.data))


class vlay:
    def Vlayout(self,url):
        self.data3=[]
        a=url
        
        while True:
            r=requests.get(a,cookies=cookies,headers=headers,timeout=5)
            soup=BS(r.content,"html.parser")
            for j in soup.find_all("div","_1sdMkc LFEi7Z"):
                # if not (j.find("div","_2ABVdq")):
                    link="https://www.flipkart.com"+j.find("a").get("href")
                    self.details_page(link)

            if soup.find("nav","WSL9JP").find_all("a")[-1].text=="Next":
                a="https://www.flipkart.com"+soup.find("nav","WSL9JP").find_all("a")[-1].get("href")
            else:
                break
        df=pd.DataFrame(self.data3)
        df.to_excel("flip2.xlsx")

    
    def details_page(self,links):
        r=requests.get(links,cookies=cookies,headers=headers,timeout=5)
        soup=BS(r.content,"html.parser")
        try:
            brand_name=soup.find("h1","_6EBuvT").find("span","mEh187").text
        except:
            brand_name="Not available"

        try:
            title=soup.find("h1","_6EBuvT").find("span","VU-ZEz").text
        except:
            title="Not available"

        try:
            rating=soup.find("div","XQDdHH").text
        except:
            rating="Not available"

        try:
            price=soup.find("div","Nx9bqj CxhGGd").text
        except:
            price="Not available"

        try:
            discount=soup.find("div","UkUFwK WW8yVX").text
        except:
            discount="Not available"

        try:
            sizes=[]
            for i in soup.find("div","OYP50x").find_all("div","_3Rka5k col col-6-12")[1]:
                for j in (i.find_all("a")):
                    sizes.append(j.text)
        except:
            sizes="Not available"

        try:
            images=[]
            for j in soup.find("div","_0J1TKd").find("ul","ZqtVYK").find_all("li"):
                images.append(j.find("img").get("src"))
        except:
            images="Not available"

        self.data3.append({
            "BRAND_NAME":brand_name,
            "TITLE":title,
            "RATING":rating,
            "PRICE":price,
            "DISCOUNT":discount,
            "STORAGE_VARIANT":sizes,
            "IMAGES_LINK":images
        })
        print(len(self.data3))


class vlay2:
    def Vlayout2(self,url):
        self.data2=[]
        a=url
        while True:
            r=requests.get(a,cookies=cookies,headers=headers,timeout=5)
            soup=BS(r.content,"html.parser")
            for i in soup.find_all("a","VJA3rP"):
                # if not (i.find("div","_2ABVdq")):
                    links=("https://www.flipkart.com"+i.get("href"))
                    self.details_page(links)
            try:
                if soup.find("nav","WSL9JP").find_all("a")[-1].text=="Next":
                    a="https://www.flipkart.com"+soup.find("nav","WSL9JP").find_all("a")[-1].get("href")
                else:
                    break
            except:
                break   
        df=pd.DataFrame(self.data2)
        df.to_excel("flip2.xlsx")

    
    def details_page(self,links):
        r=requests.get(links,cookies=cookies,headers=headers,timeout=5)
        soup=BS(r.content,"html.parser")
        try:
            brand_name=soup.find("h1","_6EBuvT").find("span","mEh187").text
        except:
            brand_name="Not available"

        try:
            title=soup.find("h1","_6EBuvT").find("span","VU-ZEz").text
        except:
            title="Not available"

        try:
            rating=soup.find("div","XQDdHH").text
        except:
            rating="Not available"

        try:
            price=soup.find("div","Nx9bqj CxhGGd").text
        except:
            price="Not available"

        try:
            discount=soup.find("div","UkUFwK WW8yVX").text
        except:
            discount="Not available"

        try:
            sizes=[]
            for i in soup.find("div","OYP50x").find_all("div","_3Rka5k col col-6-12")[1]:
                for j in (i.find_all("a")):
                    sizes.append(j.text)
        except:
            sizes="Not available"

        try:
            images=[]
            for j in soup.find("div","_0J1TKd").find("ul","ZqtVYK").find_all("li"):
                images.append(j.find("img").get("src"))
        except:
            images="Not available"

        self.data2.append({
            "BRAND_NAME":brand_name,
            "TITLE":title,
            "RATING":rating,
            "PRICE":price,
            "DISCOUNT":discount,
            "STORAGE_VARIANT":sizes,
            "IMAGES_LINK":images
        })
        print(len(self.data2))




search=input("Enter seach product--------->  ").split(",")
li=search
crl=Crawl(li)

