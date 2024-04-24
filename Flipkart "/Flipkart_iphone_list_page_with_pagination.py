import requests 
from bs4 import BeautifulSoup as BS
import time
import pandas as pd


cookies = {
    'T': 'clukuwo862mut1pdy352jcejb-BR1712212152486',
    'SN': 'VI37202652387A4B718D96FD17EE39F0E8.TOK871BC36414784F9CAF9D0822082518F1.1713590016.LO',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MTUyMzM5NDIsImlhdCI6MTcxMzUwNTk0MiwiaXNzIjoia2V2bGFyIiwianRpIjoiNDI2MGI5MDItYTgxMy00MDZiLWI5MTUtNDEwNzZhZTc2NDAxIiwidHlwZSI6IkFUIiwiZElkIjoiY2x1a3V3bzg2Mm11dDFwZHkzNTJqY2VqYi1CUjE3MTIyMTIxNTI0ODYiLCJrZXZJZCI6IlZJMzcyMDI2NTIzODdBNEI3MThEOTZGRDE3RUUzOUYwRTgiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.4dkDQpmJweXZvgKNcXa5a4lJCz_5PfB3cOJnp5KthMI',
    'K-ACTION': 'null',
    'ud': '6.TgT7YT6xQBy0GgnAGjqTbSn46hnU2pBg3Xd4bdV6xmGjk0tCnXYvkcgEceOIyrc_VpKNbz6GqponQB7xyI4GXtDlhbxgZICPzU9A48aWfUAq9SDt1bcqusIhV5dj2ME7EO3aiMKZ0VcvdpmfY2sEKw',
    'vh': '1109',
    'vw': '1499',
    'dpr': '0.8333333333333334',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19833%7CMCMID%7C00965089183736542750179575155903326637%7CMCAAMLH-1713768092%7C12%7CMCAAMB-1714107927%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1713510327s%7CNONE%7CMCAID%7CNONE',
    'rt': 'null',
    'vd': 'VI37202652387A4B718D96FD17EE39F0E8-1713505942932-4.1713590016.1713590016.151160563',
    '_pxvid': 'a83cab1c-f24c-11ee-9e01-a73a8dd08a0d',
    'S': 'd1t15Pz9wPz4/Pz8/Pz9wahELPwsb7j2PlrUIlU6Ob8x2wrYO2Of4aytl43FhE2ZZWb69PvmUP6jvhHLHGzXD3kh1Mw==',
    'fonts-loaded': 'en_loaded',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'pxcts': '2c807f69-fc8f-11ee-9c80-4f986b457776',
    'isH2EnabledBandwidth': 'true',
    'h2NetworkBandwidth': '9',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Asearch%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fapple-iphone-14-blue-256-gb%25252Fp%25252Fitm04dba659735c7%25253Fpid%25253DMOBGHWFHD3XPKDPN%252526lid%25253DLST%2526ot%253DA',
    'qH': '0b3f45b266a97d70',
    's_cc': 'true',
    '_px3': '5437bb064d80e619dbc73ba64e42397a5a7e49139f330dda82a486a2779408fa:0nUywMI19ETtgVH8rbHMQl2IoCGrrClQ8guTWF6kN9CunHRHt/W3MaNT4FSjwLNgzPGnTrX3ZUupgikzOMYfkQ==:1000:YahZkCvk9p0Ubp83PEe4sEDmitGZuzWniI07gm4F6hQchMVGcmqpj7Gzxr+tmusvLdzZiy+i+39T3mDD1HIpzuzJTpFRbFb9xowWnklauLl9f38X3Alba1ZbzsNb8KrKClU4do/lexoqEvS69Q7aqk5KrqYeS/61bpsLbWKAfMzdAGFOApb0p7zAwe26zFkUG4041UePeIvZCELSomHSREu+ZTvQZf6qGcmNZeyzu0E=',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=clukuwo862mut1pdy352jcejb-BR1712212152486; SN=VI37202652387A4B718D96FD17EE39F0E8.TOK871BC36414784F9CAF9D0822082518F1.1713590016.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MTUyMzM5NDIsImlhdCI6MTcxMzUwNTk0MiwiaXNzIjoia2V2bGFyIiwianRpIjoiNDI2MGI5MDItYTgxMy00MDZiLWI5MTUtNDEwNzZhZTc2NDAxIiwidHlwZSI6IkFUIiwiZElkIjoiY2x1a3V3bzg2Mm11dDFwZHkzNTJqY2VqYi1CUjE3MTIyMTIxNTI0ODYiLCJrZXZJZCI6IlZJMzcyMDI2NTIzODdBNEI3MThEOTZGRDE3RUUzOUYwRTgiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.4dkDQpmJweXZvgKNcXa5a4lJCz_5PfB3cOJnp5KthMI; K-ACTION=null; ud=6.TgT7YT6xQBy0GgnAGjqTbSn46hnU2pBg3Xd4bdV6xmGjk0tCnXYvkcgEceOIyrc_VpKNbz6GqponQB7xyI4GXtDlhbxgZICPzU9A48aWfUAq9SDt1bcqusIhV5dj2ME7EO3aiMKZ0VcvdpmfY2sEKw; vh=1109; vw=1499; dpr=0.8333333333333334; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19833%7CMCMID%7C00965089183736542750179575155903326637%7CMCAAMLH-1713768092%7C12%7CMCAAMB-1714107927%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1713510327s%7CNONE%7CMCAID%7CNONE; rt=null; vd=VI37202652387A4B718D96FD17EE39F0E8-1713505942932-4.1713590016.1713590016.151160563; _pxvid=a83cab1c-f24c-11ee-9e01-a73a8dd08a0d; S=d1t15Pz9wPz4/Pz8/Pz9wahELPwsb7j2PlrUIlU6Ob8x2wrYO2Of4aytl43FhE2ZZWb69PvmUP6jvhHLHGzXD3kh1Mw==; fonts-loaded=en_loaded; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; pxcts=2c807f69-fc8f-11ee-9c80-4f986b457776; isH2EnabledBandwidth=true; h2NetworkBandwidth=9; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Asearch%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fapple-iphone-14-blue-256-gb%25252Fp%25252Fitm04dba659735c7%25253Fpid%25253DMOBGHWFHD3XPKDPN%252526lid%25253DLST%2526ot%253DA; qH=0b3f45b266a97d70; s_cc=true; _px3=5437bb064d80e619dbc73ba64e42397a5a7e49139f330dda82a486a2779408fa:0nUywMI19ETtgVH8rbHMQl2IoCGrrClQ8guTWF6kN9CunHRHt/W3MaNT4FSjwLNgzPGnTrX3ZUupgikzOMYfkQ==:1000:YahZkCvk9p0Ubp83PEe4sEDmitGZuzWniI07gm4F6hQchMVGcmqpj7Gzxr+tmusvLdzZiy+i+39T3mDD1HIpzuzJTpFRbFb9xowWnklauLl9f38X3Alba1ZbzsNb8KrKClU4do/lexoqEvS69Q7aqk5KrqYeS/61bpsLbWKAfMzdAGFOApb0p7zAwe26zFkUG4041UePeIvZCELSomHSREu+ZTvQZf6qGcmNZeyzu0E=',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}


def title(soup):
    try:
        tit=soup.find("div","C7fEHH").find("h1").text
    except:
        tit="Not available"
    return tit


def rating(soup):
    try:
        rat=soup.find("div","XQDdHH").text
    except:
        rat="Not available"
    return rat


def price(soup):
    try:
        pri=soup.find("div","hl05eU").find("div","Nx9bqj CxhGGd").text
    except:
        pri="Not available"
    return pri


def discount(soup):
    try:
        dis=soup.find("div","hl05eU").find("div","UkUFwK WW8yVX").text
    except:
        dis="Not available"
    return dis


def image(soup):
    l=[]
    try:
        for i in soup.find("ul","ZqtVYK").find_all("li"):
            l.append(i.find("img").get("src"))
    except:
        None
    return l



url="https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
l=[]
while True:
    print(url)
    r = requests.get(url, cookies=cookies, headers=headers)
    soup=BS(r.content,"html.parser")
    for j in soup.find_all("div","tUxRFH"):
        link="https://www.flipkart.com"+(j.find("a").get("href"))
        re=requests.get(link,cookies=cookies, headers=headers)
        soup1=BS(re.content,"html.parser")
        tit=title(soup1)
        rat=rating(soup1)
        pri=price(soup1)
        dis=discount(soup1)
        img=image(soup1)
        l.append({
            "TITLE":tit,
            "RATING":rat,
            "PRICE":pri,
            "DISCOUNT":dis,
            "IMAGES_LINK":img,
            "LINK":link
        })
    # print(url,l,sep="-------------")
    if soup.find("nav","WSL9JP").find_all("a")[-1].text=="Next":
        url="https://www.flipkart.com"+soup.find("nav","WSL9JP").find_all("a")[-1].get("href")
    else:
        break



# l=[]
# r=requests.get("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1",cookies=cookies, headers=headers)
# soup=BS(r.content,"html.parser")
# aa=int(soup.find("div","_1G0WLw").find("span").text.split()[-1])
# for i in range(1,aa+1):
#     print(i)
#     url=f"https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
#     r=requests.get(url,cookies=cookies, headers=headers)
#     soup=BS(r.content,"html.parser")
#     for j in soup.find_all("div","tUxRFH"):
#         link="https://www.flipkart.com"+(j.find("a").get("href"))
#         re=requests.get(link,cookies=cookies, headers=headers)
#         soup=BS(re.content,"html.parser")
#         tit=title(soup)
#         rat=rating(soup)
#         pri=price(soup)
#         dis=discount(soup)
#         img=image(soup)
#         l.append({
#             "TITLE":tit,
#             "RATING":rat,
#             "PRICE":pri,
#             "DISCOUNT":dis,
#             "IMAGES_LINK":img,
#             "LINK":link
#         })

df=pd.DataFrame(l)
df.to_excel("flip.xlsx")
