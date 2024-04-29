import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

cookies = {
    'T': 'clukuwo862mut1pdy352jcejb-BR1712212152486',
    'SN': 'VI37202652387A4B718D96FD17EE39F0E8.TOK871BC36414784F9CAF9D0822082518F1.1714366553.LO',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MTUyMzM5NDIsImlhdCI6MTcxMzUwNTk0MiwiaXNzIjoia2V2bGFyIiwianRpIjoiNDI2MGI5MDItYTgxMy00MDZiLWI5MTUtNDEwNzZhZTc2NDAxIiwidHlwZSI6IkFUIiwiZElkIjoiY2x1a3V3bzg2Mm11dDFwZHkzNTJqY2VqYi1CUjE3MTIyMTIxNTI0ODYiLCJrZXZJZCI6IlZJMzcyMDI2NTIzODdBNEI3MThEOTZGRDE3RUUzOUYwRTgiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.4dkDQpmJweXZvgKNcXa5a4lJCz_5PfB3cOJnp5KthMI',
    'K-ACTION': 'null',
    'ud': '6.TgT7YT6xQBy0GgnAGjqTbSn46hnU2pBg3Xd4bdV6xmGjk0tCnXYvkcgEceOIyrc_VpKNbz6GqponQB7xyI4GXtDlhbxgZICPzU9A48aWfUAq9SDt1bcqusIhV5dj2ME7EO3aiMKZ0VcvdpmfY2sEKw',
    'vh': '1232',
    'vw': '2560',
    'dpr': '0.75',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19843%7CMCMID%7C00965089183736542750179575155903326637%7CMCAAMLH-1714373085%7C12%7CMCAAMB-1714971310%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1714373710s%7CNONE%7CMCAID%7CNONE',
    'rt': 'null',
    'vd': 'VI37202652387A4B718D96FD17EE39F0E8-1713505942932-26.1714366507.1714366507.155371378',
    '_pxvid': 'a83cab1c-f24c-11ee-9e01-a73a8dd08a0d',
    'S': 'd1t15P3UmJm8vP3BaQz8/Py5NM3715zDRz8WJMrX5kifpEd01P5Id42L3iht80wk2q7ATWby+g4hPDsFDX9S/UWHqXA==',
    '_gcl_au': '1.1.441939276.1714057074',
    '_px3': '6127837500f3ee376eb21d37997c64933e6753fbcffe7800af94bcba1b1b7807:OY4F6NdViB1bkksOA3+Iw8wReAhSAL19rq5ns5ZlpQJnY/gxj9Pvw9HOsdSw6J37kWLkQ/34yZCWQcsaaqit3w==:1000:nw0qUXHP5VxL+ZRM2Raf90bmB0Bn8XJ0xV7Fblmi/CSRp7+k8of75f57h+Aki/hTU0hdOZifO/VJ0EahZmdA98MNaWHLBKeo+hHMpzyxjBGYzqpgfBAn702kZqBrRGGhAOLaRwP6IUHIiX39gVb4oE7uQcswWgy4aMGJVXsxiLonWYcbNUsMceuskbvKCh3BeP6v2Yev9tTXfugcJqgNoqfeTmlGaiTkJ50kpfR4IJ8=',
    'fonts-loaded': 'en_loaded',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'isH2EnabledBandwidth': 'true',
    'h2NetworkBandwidth': '9',
    'pxcts': 'a8222d6c-05e4-11ef-8db0-fc2affa1e3d6',
    'gpv_pn': 'HomePage',
    'gpv_pn_t': 'FLIPKART%3AHomePage',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Amobile-phones-store%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fapple-iphone-14-blue-128-gb%25252Fp%25252Fitmdb77f40da6b6d%25253Fpid%25253DMOBGHWFHSV7GUFWA%252526lid%25253DLST%2526ot%253DA',
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
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=clukuwo862mut1pdy352jcejb-BR1712212152486; SN=VI37202652387A4B718D96FD17EE39F0E8.TOK871BC36414784F9CAF9D0822082518F1.1714366553.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MTUyMzM5NDIsImlhdCI6MTcxMzUwNTk0MiwiaXNzIjoia2V2bGFyIiwianRpIjoiNDI2MGI5MDItYTgxMy00MDZiLWI5MTUtNDEwNzZhZTc2NDAxIiwidHlwZSI6IkFUIiwiZElkIjoiY2x1a3V3bzg2Mm11dDFwZHkzNTJqY2VqYi1CUjE3MTIyMTIxNTI0ODYiLCJrZXZJZCI6IlZJMzcyMDI2NTIzODdBNEI3MThEOTZGRDE3RUUzOUYwRTgiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.4dkDQpmJweXZvgKNcXa5a4lJCz_5PfB3cOJnp5KthMI; K-ACTION=null; ud=6.TgT7YT6xQBy0GgnAGjqTbSn46hnU2pBg3Xd4bdV6xmGjk0tCnXYvkcgEceOIyrc_VpKNbz6GqponQB7xyI4GXtDlhbxgZICPzU9A48aWfUAq9SDt1bcqusIhV5dj2ME7EO3aiMKZ0VcvdpmfY2sEKw; vh=1232; vw=2560; dpr=0.75; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19843%7CMCMID%7C00965089183736542750179575155903326637%7CMCAAMLH-1714373085%7C12%7CMCAAMB-1714971310%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1714373710s%7CNONE%7CMCAID%7CNONE; rt=null; vd=VI37202652387A4B718D96FD17EE39F0E8-1713505942932-26.1714366507.1714366507.155371378; _pxvid=a83cab1c-f24c-11ee-9e01-a73a8dd08a0d; S=d1t15P3UmJm8vP3BaQz8/Py5NM3715zDRz8WJMrX5kifpEd01P5Id42L3iht80wk2q7ATWby+g4hPDsFDX9S/UWHqXA==; _gcl_au=1.1.441939276.1714057074; _px3=6127837500f3ee376eb21d37997c64933e6753fbcffe7800af94bcba1b1b7807:OY4F6NdViB1bkksOA3+Iw8wReAhSAL19rq5ns5ZlpQJnY/gxj9Pvw9HOsdSw6J37kWLkQ/34yZCWQcsaaqit3w==:1000:nw0qUXHP5VxL+ZRM2Raf90bmB0Bn8XJ0xV7Fblmi/CSRp7+k8of75f57h+Aki/hTU0hdOZifO/VJ0EahZmdA98MNaWHLBKeo+hHMpzyxjBGYzqpgfBAn702kZqBrRGGhAOLaRwP6IUHIiX39gVb4oE7uQcswWgy4aMGJVXsxiLonWYcbNUsMceuskbvKCh3BeP6v2Yev9tTXfugcJqgNoqfeTmlGaiTkJ50kpfR4IJ8=; fonts-loaded=en_loaded; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; isH2EnabledBandwidth=true; h2NetworkBandwidth=9; pxcts=a8222d6c-05e4-11ef-8db0-fc2affa1e3d6; gpv_pn=HomePage; gpv_pn_t=FLIPKART%3AHomePage; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Amobile-phones-store%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fapple-iphone-14-blue-128-gb%25252Fp%25252Fitmdb77f40da6b6d%25253Fpid%25253DMOBGHWFHSV7GUFWA%252526lid%25253DLST%2526ot%253DA; qH=0b3f45b266a97d70',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

d=[]
q=0
url='https://www.flipkart.com/apple-iphone-14-blue-128-gb/product-reviews/itmdb77f40da6b6d?pid=MOBGHWFHSV7GUFWA&lid=LSTMOBGHWFHSV7GUFWAFEQJQ4&marketplace=FLIPKART'
while True:
    if q==2:
        break
    q+=1        
    print(url)
    response = requests.get(url,cookies=cookies,headers=headers,)
    soup=BS(response.content,"html.parser")
    for i in soup.find_all("div","col EPCmJX Ma1fCG"):
        try:
            rating=(i.find("div","XQDdHH Ga3i8K").text)
        except:
            rating=None

        try:
            rating_title=(i.find("p","z9E0IG").text)
        except:
            rating_title=None

        try:
            comments=(i.find("div","ZmyHeo").text.replace("READ MORE",""))
        except:
            comments=None

        try:
            custome_name=(i.find("p","_2NsDsF AwS1CA").text)
        except:
            custome_name=None

        try:
            certified_user=(i.find("p","MztJPv").find_all("span")[0].text)
        except:
            certified_user=None

        try:
            address=(i.find("p","MztJPv").find_all("span")[1].text.replace(",",""))
        except:
            address=None

        try:
            update_time=(i.find_all("p")[-1].text)
        except:
            update_time=None

        try:
            likes=(i.find("div","_6kK6mk").find("span","tl9VpF").text)
        except:
            likes=None

        try:
            dislikes=(i.find("div","_6kK6mk aQymJL").find("span","tl9VpF").text)
        except:
            dislikes=None

        try:
            images=[]
            for j in (i.find("div","xmAgz5 pVVA7t").find_all("div","Be4x5X d517go")):
                images.append(j.get("style").split(",")[0].replace("background-image:url",""))
        except:
            images=None


        d.append({
        "RATING":rating,
        "RATING_TITLE":rating_title,
        "COMMENTS":comments,
        "CUSTOMER_NAME":custome_name,
        "CERTIFIED_USER":certified_user,
        "ADDRESS":address,
        "UPDATE_TIME":update_time,
        "LIKES":likes,
        "DISLIKES":dislikes,
        "IMAGES":images
        })
    if soup.find("nav","WSL9JP").find_all("a")[-1].text=="Next":
        url="https://www.flipkart.com"+soup.find("nav","WSL9JP").find_all("a")[-1].get("href")
    else:
        break

df=pd.DataFrame(d)
df.to_excel("flp.xlsx")
