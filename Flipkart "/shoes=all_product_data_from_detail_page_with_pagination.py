
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

cookies = {
    'T': 'clukuwo862mut1pdy352jcejb-BR1712212152486',
    'SN': 'VI37202652387A4B718D96FD17EE39F0E8.TOK871BC36414784F9CAF9D0822082518F1.1713846461.LO',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MTUyMzM5NDIsImlhdCI6MTcxMzUwNTk0MiwiaXNzIjoia2V2bGFyIiwianRpIjoiNDI2MGI5MDItYTgxMy00MDZiLWI5MTUtNDEwNzZhZTc2NDAxIiwidHlwZSI6IkFUIiwiZElkIjoiY2x1a3V3bzg2Mm11dDFwZHkzNTJqY2VqYi1CUjE3MTIyMTIxNTI0ODYiLCJrZXZJZCI6IlZJMzcyMDI2NTIzODdBNEI3MThEOTZGRDE3RUUzOUYwRTgiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.4dkDQpmJweXZvgKNcXa5a4lJCz_5PfB3cOJnp5KthMI',
    'K-ACTION': 'null',
    'ud': '6.TgT7YT6xQBy0GgnAGjqTbSn46hnU2pBg3Xd4bdV6xmGjk0tCnXYvkcgEceOIyrc_VpKNbz6GqponQB7xyI4GXtDlhbxgZICPzU9A48aWfUAq9SDt1bcqusIhV5dj2ME7EO3aiMKZ0VcvdpmfY2sEKw',
    'vh': '1109',
    'vw': '2304',
    'dpr': '0.8333333333333334',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19837%7CMCMID%7C00965089183736542750179575155903326637%7CMCAAMLH-1714373085%7C12%7CMCAAMB-1714451254%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1713853654s%7CNONE%7CMCAID%7CNONE',
    'rt': 'null',
    'vd': 'VI37202652387A4B718D96FD17EE39F0E8-1713505942932-12.1713846449.1713846449.155371390',
    '_pxvid': 'a83cab1c-f24c-11ee-9e01-a73a8dd08a0d',
    'S': 'd1t15Pz8/OiZwJFQ/P30/P1Q/P9/3lCPjy2wzZQc+aGinQMkr0uEdvkCBCvQR9k9fngmNM4d7AelB7ekSPrWezcuAtA==',
    'pxcts': '8abcc49b-ff53-11ee-8709-fc05767f0932',
    's_sq': 'flipkart-prd%3D%2526pid%253DHomePage%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fmens-tshirts%25252Fpr%25253Fsid%25253Dclo%25252Cash%25252Cank%25252Cedy%252526fm%25253Dneo%2525252Fmerchandising%252526iid%25253DM_b9aa0b75-a%2526ot%253DA',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'fonts-loaded': 'en_loaded',
    'isH2EnabledBandwidth': 'true',
    'h2NetworkBandwidth': '9',
    '_px3': 'be009a09d5686589840ef0dd9bc702d1c2e1c8c8a37d6987cd39ee0948277d92:/VE01gSM9a0AfyTU/ztuGSzED6ND9d8c/o0SWgmdtlImqvDYwbonXZAf/HpPvh7e8197XxIizW6m6VAz2ZBbMA==:1000:pScPDUiE8Weq2HWYUj4PNJnaMVQPcQktKKT7nX0+xl7pb/YFBkov8hprwjrDyShbynyH9S7FP4kDNT2S/qC+zFsLyVzzpyApw0g1XCR3M1LjE61zOcrZAeYKVanE5/nHXqWAxIvo1shq29aYdGXCdoyhaQWGhUuy8O8vQU34aG5g7CfCKUzN+Yg2VzOb0fT73VDl05UgleARsjKlA09BkaStoJJd+HIUvVaBDo6iTMo=',
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
    # 'Cookie': 'T=clukuwo862mut1pdy352jcejb-BR1712212152486; SN=VI37202652387A4B718D96FD17EE39F0E8.TOK871BC36414784F9CAF9D0822082518F1.1713846461.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MTUyMzM5NDIsImlhdCI6MTcxMzUwNTk0MiwiaXNzIjoia2V2bGFyIiwianRpIjoiNDI2MGI5MDItYTgxMy00MDZiLWI5MTUtNDEwNzZhZTc2NDAxIiwidHlwZSI6IkFUIiwiZElkIjoiY2x1a3V3bzg2Mm11dDFwZHkzNTJqY2VqYi1CUjE3MTIyMTIxNTI0ODYiLCJrZXZJZCI6IlZJMzcyMDI2NTIzODdBNEI3MThEOTZGRDE3RUUzOUYwRTgiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.4dkDQpmJweXZvgKNcXa5a4lJCz_5PfB3cOJnp5KthMI; K-ACTION=null; ud=6.TgT7YT6xQBy0GgnAGjqTbSn46hnU2pBg3Xd4bdV6xmGjk0tCnXYvkcgEceOIyrc_VpKNbz6GqponQB7xyI4GXtDlhbxgZICPzU9A48aWfUAq9SDt1bcqusIhV5dj2ME7EO3aiMKZ0VcvdpmfY2sEKw; vh=1109; vw=2304; dpr=0.8333333333333334; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19837%7CMCMID%7C00965089183736542750179575155903326637%7CMCAAMLH-1714373085%7C12%7CMCAAMB-1714451254%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1713853654s%7CNONE%7CMCAID%7CNONE; rt=null; vd=VI37202652387A4B718D96FD17EE39F0E8-1713505942932-12.1713846449.1713846449.155371390; _pxvid=a83cab1c-f24c-11ee-9e01-a73a8dd08a0d; S=d1t15Pz8/OiZwJFQ/P30/P1Q/P9/3lCPjy2wzZQc+aGinQMkr0uEdvkCBCvQR9k9fngmNM4d7AelB7ekSPrWezcuAtA==; pxcts=8abcc49b-ff53-11ee-8709-fc05767f0932; s_sq=flipkart-prd%3D%2526pid%253DHomePage%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fmens-tshirts%25252Fpr%25253Fsid%25253Dclo%25252Cash%25252Cank%25252Cedy%252526fm%25253Dneo%2525252Fmerchandising%252526iid%25253DM_b9aa0b75-a%2526ot%253DA; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; fonts-loaded=en_loaded; isH2EnabledBandwidth=true; h2NetworkBandwidth=9; _px3=be009a09d5686589840ef0dd9bc702d1c2e1c8c8a37d6987cd39ee0948277d92:/VE01gSM9a0AfyTU/ztuGSzED6ND9d8c/o0SWgmdtlImqvDYwbonXZAf/HpPvh7e8197XxIizW6m6VAz2ZBbMA==:1000:pScPDUiE8Weq2HWYUj4PNJnaMVQPcQktKKT7nX0+xl7pb/YFBkov8hprwjrDyShbynyH9S7FP4kDNT2S/qC+zFsLyVzzpyApw0g1XCR3M1LjE61zOcrZAeYKVanE5/nHXqWAxIvo1shq29aYdGXCdoyhaQWGhUuy8O8vQU34aG5g7CfCKUzN+Yg2VzOb0fT73VDl05UgleARsjKlA09BkaStoJJd+HIUvVaBDo6iTMo=',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}





def list_page_links(soup):
    l=[]
    for i in soup.find_all("a","rPDeLR"):
        l.append("https://www.flipkart.com"+i.get("href"))
    return (l)


url="https://www.flipkart.com/mens-footwear/sports-shoes/pr?sid=osp%2Ccil%2C1cu&otracker=nmenu_sub_Men_0_Sports+Shoes"
l1=[]
while True:
    response = requests.get(url,cookies=cookies,headers=headers)
    print(url)
    soup=BS(response.content,"html.parser")
    l=list_page_links(soup)
    for i in l:
        r=requests.get(i,cookies=cookies,headers=headers)
        soup2=BS(r.content,"html.parser")

        try:
            brand_name=soup2.find("h1").find("span","mEh187").text.strip()
        except:
            brand_name="Not available"

        try:
            name=soup2.find("h1").find("span","VU-ZEz").text.replace("\xa0\xa0"," ")
        except:
            name="Not available"
        

        try:
            price=soup2.find("div","hl05eU").find("div","Nx9bqj CxhGGd").text 
        except:
            price="Not available"

        try:
            discount=soup2.find("div","hl05eU").find("div","UkUFwK WW8yVX dB67CR").text
        except:
            discount="Not available"

        try:
            rating= soup2.find("div","XQDdHH _1Quie7").text
        except:
            rating="Not available"


        l1.append({
            "Brand_Name":brand_name,
            "Product_Name":name,
            "Price":price,
            "Discount":discount,
            "Rating":rating
        })
    try:
        if soup.find("nav","WSL9JP").find_all("a")[-1].text=="Next":
            url="https://www.flipkart.com"+soup.find("nav","WSL9JP").find_all("a")[-1].get("href")
        else:
            break
    except:
        break


df=pd.DataFrame(l1)
df.to_excel("flip2.xlsx",index=False)
