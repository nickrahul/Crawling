from bs4 import BeautifulSoup as BS
import requests
import pandas as pd

cookies = {
    'T': 'clukuwo862mut1pdy352jcejb-BR1712212152486',
    'SN': 'VI37202652387A4B718D96FD17EE39F0E8.TOK871BC36414784F9CAF9D0822082518F1.1714024550.LO',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MTUyMzM5NDIsImlhdCI6MTcxMzUwNTk0MiwiaXNzIjoia2V2bGFyIiwianRpIjoiNDI2MGI5MDItYTgxMy00MDZiLWI5MTUtNDEwNzZhZTc2NDAxIiwidHlwZSI6IkFUIiwiZElkIjoiY2x1a3V3bzg2Mm11dDFwZHkzNTJqY2VqYi1CUjE3MTIyMTIxNTI0ODYiLCJrZXZJZCI6IlZJMzcyMDI2NTIzODdBNEI3MThEOTZGRDE3RUUzOUYwRTgiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.4dkDQpmJweXZvgKNcXa5a4lJCz_5PfB3cOJnp5KthMI',
    'K-ACTION': 'null',
    'ud': '6.TgT7YT6xQBy0GgnAGjqTbSn46hnU2pBg3Xd4bdV6xmGjk0tCnXYvkcgEceOIyrc_VpKNbz6GqponQB7xyI4GXtDlhbxgZICPzU9A48aWfUAq9SDt1bcqusIhV5dj2ME7EO3aiMKZ0VcvdpmfY2sEKw',
    'vh': '1109',
    'vw': '2304',
    'dpr': '0.8333333333333334',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19839%7CMCMID%7C00965089183736542750179575155903326637%7CMCAAMLH-1714373085%7C12%7CMCAAMB-1714629203%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1714031603s%7CNONE%7CMCAID%7CNONE',
    'rt': 'null',
    'vd': 'VI37202652387A4B718D96FD17EE39F0E8-1713505942932-16.1714024602.1714024399.155117403',
    '_pxvid': 'a83cab1c-f24c-11ee-9e01-a73a8dd08a0d',
    'S': 'd1t15Pz8PPws3P0E/P2EZbT8/P2IWuYzDQlzY8uuWjam8IrDCINGa0VM08OCRLD2wuN3np04XdTaCJcfUC6oxJT0R0w==',
    '_px3': 'b871467eea90c0435a2b9e770fcc663debd0e76760679fec9ebe922ce62a919f:tcN3DLhUb6YXWRZ0gnao9PoAdLqMc6qI0kzZwtpPfdmDhgSA230KDDbx1waNEnra9SQLRYo8TMqtp7r8Jcq0HQ==:1000:0a2HRE37+JQpDPGFFyYqYKsWlBTcHO49Y7hU+IP9HS2rpsHUDUY6m/gaX9UnvYoAcL4dOlUkzP+sDVUBdmv98u3sL1h/yAIZF1CJCjrDOF3A68ej/mm6mI/MIyDN5+uzi/B263LIfQdufQ/DNoiYxgsmThTUmEfkbHm2Yh1kN0/XzvfsrV0cYE129SmH+As2WI5xrdL4/EOMM8z7vcU2gCdCQP6SoOaTvtd7DUo65hY=',
    'pxcts': '8abcc49b-ff53-11ee-8709-fc05767f0932',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Atvs-and-appliances-new-clp-store%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Findustrial-scientific-supplies%25252Findustrial-measurement-devices%25252Fsound-meters%25252F%2526ot%253DA',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'fonts-loaded': 'en_loaded',
    'isH2EnabledBandwidth': 'true',
    'h2NetworkBandwidth': '9',
    'gpv_pn': 'HomePage',
    'gpv_pn_t': 'FLIPKART%3AHomePage',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.flipkart.com/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=clukuwo862mut1pdy352jcejb-BR1712212152486; SN=VI37202652387A4B718D96FD17EE39F0E8.TOK871BC36414784F9CAF9D0822082518F1.1714024550.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MTUyMzM5NDIsImlhdCI6MTcxMzUwNTk0MiwiaXNzIjoia2V2bGFyIiwianRpIjoiNDI2MGI5MDItYTgxMy00MDZiLWI5MTUtNDEwNzZhZTc2NDAxIiwidHlwZSI6IkFUIiwiZElkIjoiY2x1a3V3bzg2Mm11dDFwZHkzNTJqY2VqYi1CUjE3MTIyMTIxNTI0ODYiLCJrZXZJZCI6IlZJMzcyMDI2NTIzODdBNEI3MThEOTZGRDE3RUUzOUYwRTgiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.4dkDQpmJweXZvgKNcXa5a4lJCz_5PfB3cOJnp5KthMI; K-ACTION=null; ud=6.TgT7YT6xQBy0GgnAGjqTbSn46hnU2pBg3Xd4bdV6xmGjk0tCnXYvkcgEceOIyrc_VpKNbz6GqponQB7xyI4GXtDlhbxgZICPzU9A48aWfUAq9SDt1bcqusIhV5dj2ME7EO3aiMKZ0VcvdpmfY2sEKw; vh=1109; vw=2304; dpr=0.8333333333333334; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19839%7CMCMID%7C00965089183736542750179575155903326637%7CMCAAMLH-1714373085%7C12%7CMCAAMB-1714629203%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1714031603s%7CNONE%7CMCAID%7CNONE; rt=null; vd=VI37202652387A4B718D96FD17EE39F0E8-1713505942932-16.1714024602.1714024399.155117403; _pxvid=a83cab1c-f24c-11ee-9e01-a73a8dd08a0d; S=d1t15Pz8PPws3P0E/P2EZbT8/P2IWuYzDQlzY8uuWjam8IrDCINGa0VM08OCRLD2wuN3np04XdTaCJcfUC6oxJT0R0w==; _px3=b871467eea90c0435a2b9e770fcc663debd0e76760679fec9ebe922ce62a919f:tcN3DLhUb6YXWRZ0gnao9PoAdLqMc6qI0kzZwtpPfdmDhgSA230KDDbx1waNEnra9SQLRYo8TMqtp7r8Jcq0HQ==:1000:0a2HRE37+JQpDPGFFyYqYKsWlBTcHO49Y7hU+IP9HS2rpsHUDUY6m/gaX9UnvYoAcL4dOlUkzP+sDVUBdmv98u3sL1h/yAIZF1CJCjrDOF3A68ej/mm6mI/MIyDN5+uzi/B263LIfQdufQ/DNoiYxgsmThTUmEfkbHm2Yh1kN0/XzvfsrV0cYE129SmH+As2WI5xrdL4/EOMM8z7vcU2gCdCQP6SoOaTvtd7DUo65hY=; pxcts=8abcc49b-ff53-11ee-8709-fc05767f0932; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Atvs-and-appliances-new-clp-store%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Findustrial-scientific-supplies%25252Findustrial-measurement-devices%25252Fsound-meters%25252F%2526ot%253DA; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; fonts-loaded=en_loaded; isH2EnabledBandwidth=true; h2NetworkBandwidth=9; gpv_pn=HomePage; gpv_pn_t=FLIPKART%3AHomePage',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

class crawling:
    def __init__(self,url) -> None:
        self.url=url
        response=requests.get(self.url,cookies=cookies,headers=headers,timeout=5)
        soup=BS(response.content,"html.parser")
        self.list_page(soup)

    
    def list_page(self,soup):
        self.data=[]
        a=self.url
        while True:
            response=requests.get(a,cookies=cookies,headers=headers,timeout=5)
            soup=BS(response.content,"html.parser")
            for i in soup.find_all("div","slAVV4"):
                link="https://www.flipkart.com"+i.find("a").get("href")
                self.detail_page(link)
            
            if soup.find("nav","WSL9JP").find_all("a")[-1].text=='Next':
                a="https://www.flipkart.com"+soup.find("nav","WSL9JP").find_all("a")[-1].get("href")
            else:
                break
        df=pd.DataFrame(self.data)
        df.to_excel("flip.xlsx",index=False)
    
    def detail_page(self,link):
            r=requests.get(link,cookies=cookies,headers=headers,timeout=5)
            soup2=BS(r.content,"html.parser")
            try:
                title=soup2.find("div","C7fEHH").find("h1").text
            except:
                title="Not available"
            
            try:
                rating=soup2.find("div","XQDdHH").text
            except:
                rating="Not available"

            try:
                current_price=soup2.find("div","Nx9bqj CxhGGd").text
            except:
                current_price="Not available"

            try:
                old_price=soup2.find("div","yRaY8j A6+E6v").text
            except:
                old_price="Not abvailble"

            try:
                discount=soup2.find("div","UkUFwK WW8yVX").text
            except:
                discount="Not available"

            try:
                l1=[]
                for i in soup2.find("div","I+EQVr").find_all("span","+-2B3d row"):
                    l1.append(i.text.replace("Bank Offer","").replace("T&C",""))
            except:
                l1="Not available"

            try:
                dic={}

                for i in soup2.find_all("div","GNDEQ-"):
                    ta=i.find("div","_4BJ2V+").text
                    if ta=="General":
                        table=i.find("table","_0ZhAN9")
                        for i in table.find_all("tr"):
                            data1=(i.find("td","+fFi1w col col-3-12"))
                            data2=(i.find("td","Izz52n col col-9-12"))
                            dic.update({data1.text:data2.text})
                    
            except:
                dic="Not available"
            
            self.data.append({
                "TITLE":title,
                "RATING":rating,
                "CURRENT_PRICE":current_price,
                "OLD_PRICE":old_price,
                "DISCOUNT":discount,
                "OFFERS":l1,
                "SPECIFICATION":dic
            })


craw=crawling("https://www.flipkart.com/industrial-scientific-supplies/industrial-measurement-devices/sound-meters/pr?sid=gsx,oe8,lab&otracker=categorytree")
