
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

cookies = {
    'vrid': '1d20af84-8541-4d53-b8b3-689e0ca39f1d',
    'express:sess': 'eyJka3MiOiI5NWU2MGRkMC04MjE4LTQxZGMtOGY0Yi1hNzY0NmJkNDBjODYiLCJtYXJrZXRpbmciOnt9LCJmbGFzaCI6e319',
    'express:sess.sig': 'IX1lhGha7UHw4emrXkW9Q4ZiEgg',
    'AMCV_A57E776A5245AEA80A490D44%40AdobeOrg': '-1303530583%7CMCIDTS%7C19836%7CMCMID%7C25076041132398538770534284749673269922%7CMCAID%7CNONE%7CMCOPTOUT-1713863989s%7CNONE%7CMCAAMLH-1714461589%7C12%7CMCAAMB-1714461589%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C3.3.0%7CMCSYNCSOP%7C411-19843',
    '_ga_0EQTJQH34W': 'GS1.1.1713856788.12.1.1713856800.48.0.0',
    '_ga': 'GA1.1.1971223221.1712993042',
    's_ecid': 'MCMID%7C25076041132398538770534284749673269922',
    's_nr': '1712997753935',
    's_prop70': 'April',
    's_prop71': '15',
    '__gads': 'ID=67a937aa316eb0f2:T=1712993502:RT=1713818782:S=ALNI_MY3XTDnQO9cl5vQbu3kS0IaxWpQWA',
    '__gpi': 'UID=00000deb22a9632f:T=1712993502:RT=1713818782:S=ALNI_MaVdEj-5a8jz70GwfnZ4-y8hqq_1A',
    '__eoi': 'ID=c1379e9a6f91adbe:T=1712993502:RT=1713818782:S=AA-AfjYoRu66DApTSw-RwtPiUrz1',
    '__gsas': 'ID=b6fd72025f47cf4a:T=1712997012:RT=1712997012:S=ALNI_MYzWtBxsOIlxgX5lOBb1dtlANYOeQ',
    's_otb': 'false',
    'zone': '330',
    'AMCVS_A57E776A5245AEA80A490D44%40AdobeOrg': '1',
    's_ppv': 'home.htm%2C26%2C26%2C864',
    's_tp': '3376',
    's_cc': 'true',
    's_sq': '%5B%5BB%5D%5D',
    'sorted': 'false',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.yellowpages.com/los-angeles-ca/restaurants?page=1',
    'Connection': 'keep-alive',
    # 'Cookie': 'vrid=1d20af84-8541-4d53-b8b3-689e0ca39f1d; express:sess=eyJka3MiOiI5NWU2MGRkMC04MjE4LTQxZGMtOGY0Yi1hNzY0NmJkNDBjODYiLCJtYXJrZXRpbmciOnt9LCJmbGFzaCI6e319; express:sess.sig=IX1lhGha7UHw4emrXkW9Q4ZiEgg; AMCV_A57E776A5245AEA80A490D44%40AdobeOrg=-1303530583%7CMCIDTS%7C19836%7CMCMID%7C25076041132398538770534284749673269922%7CMCAID%7CNONE%7CMCOPTOUT-1713863989s%7CNONE%7CMCAAMLH-1714461589%7C12%7CMCAAMB-1714461589%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C3.3.0%7CMCSYNCSOP%7C411-19843; _ga_0EQTJQH34W=GS1.1.1713856788.12.1.1713856800.48.0.0; _ga=GA1.1.1971223221.1712993042; s_ecid=MCMID%7C25076041132398538770534284749673269922; s_nr=1712997753935; s_prop70=April; s_prop71=15; __gads=ID=67a937aa316eb0f2:T=1712993502:RT=1713818782:S=ALNI_MY3XTDnQO9cl5vQbu3kS0IaxWpQWA; __gpi=UID=00000deb22a9632f:T=1712993502:RT=1713818782:S=ALNI_MaVdEj-5a8jz70GwfnZ4-y8hqq_1A; __eoi=ID=c1379e9a6f91adbe:T=1712993502:RT=1713818782:S=AA-AfjYoRu66DApTSw-RwtPiUrz1; __gsas=ID=b6fd72025f47cf4a:T=1712997012:RT=1712997012:S=ALNI_MYzWtBxsOIlxgX5lOBb1dtlANYOeQ; s_otb=false; zone=330; AMCVS_A57E776A5245AEA80A490D44%40AdobeOrg=1; s_ppv=home.htm%2C26%2C26%2C864; s_tp=3376; s_cc=true; s_sq=%5B%5BB%5D%5D; sorted=false',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}


def get_all_link_from_main_page(soup):
    l=["https://www.yellowpages.com"+i.get("href") for i in soup.find("section",id="quick-search").find_all("a") if i.get("href")!="https://people.yellowpages.com/whitepages"]
    list_page(l)

def list_page(l):
    l1=[]
    a=l[0]
    while True:
        r=requests.get(a ,cookies=cookies,headers=headers)
        print(a)
        soup=BS(r.content,"html.parser")
        for i in soup.find("div","search-results organic").find_all("div","v-card"):
            links="https://www.yellowpages.com"+i.find("h2").find("a").get("href")
            r1=requests.get(links ,cookies=cookies,headers=headers)
            soup2=BS(r1.content,"html.parser")
            try:
                Name=soup2.find("div","sales-info").find("h1").text
            except:
                Name="Not available"
            
            try:
                categories=soup2.find("div","mobile-claimed-category").find("div","categories").text
            except:
                categories="Not available"

            try:
                if soup2.find("section","ratings").text=="Be the first to review on YP!":
                    ratings="Not available"
                else:
                    ratings=soup2.find("section","ratings").text
            except:
                ratings="Not available"

            try:
                phone=soup2.find("a","phone dockable").text
            except:
                phone="Not available"

            try:
                address=soup2.find("span","address").text
            except:
                address="Not available"
            
            try:
                website_link=soup2.find("a","website-link dockable").get("href")
            except:
                website_link="Not available"
            
            l1.append({
                "NAME":Name,
                "CATEGORIES":categories,
                "RATINGS":ratings,
                "PHONE":phone,
                "ADDRESS":address,
                "WEBSITE_LINK":website_link
            })
        print(len(l1))
        if soup.find("a","next ajax-page").text=='Next':
            a="https://www.yellowpages.com"+soup.find("a","next ajax-page").get("href")
        else:
            break
    df=pd.DataFrame(l1)
    df.to_excel("rahul.xlsx")   

    


url="https://www.yellowpages.com/"
r=requests.get(url,cookies=cookies,headers=headers)
soup=BS(r.content,"html.parser")
get_all_link_from_main_page(soup)

