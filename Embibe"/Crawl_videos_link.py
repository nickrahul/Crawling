
import requests
from bs4 import BeautifulSoup as BS
# from crawl import crawl
import pandas as pd

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
     'Accept': 'application/json, text/plain, */*',
     'Accept-Language': 'en-US,en;q=0.5',
     # 'Accept-Encoding': 'gzip, deflate, br',
     'embibe-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJjb3VudHJ5IjoxLCJ1c2VyX3R5cGUiOjEsImNyZWF0ZWQiOjE2ODY2NDk1NDIsIm9yZ2FuaXphdGlvbl9pZCI6IjEiLCJpZCI6MjAxNjE1NjUxOCwiZXhwIjoxNzE3NDA3OTQyLCJkZXZpY2VJZCI6InBsYXRfMTNfanVuXzE2ODU2MjkwNzYwMjM0IiwibW9iaWxlX3ZlcmlmaWNhdGlvbl9zdGF0dXMiOmZhbHNlLCJlbWFpbF92ZXJpZmljYXRpb25fc3RhdHVzIjp0cnVlLCJlbWFpbCI6InBsYXRmb3JtQGVtYmliZS5jb20ifQ.S1XIlJd4LUuHOq5J_ODFVI8E1JqSAAlpnHaNq80R53KjVuwomwVZUb0QtaNZ6HG7GqbSzpqrJv3eh1gpqr8pdw',
     'Origin': 'https://www.embibe.com',
     'Connection': 'keep-alive',
     'Referer': 'https://www.embibe.com/',
     'Sec-Fetch-Dest': 'empty',
     'Sec-Fetch-Mode': 'cors',
     'Sec-Fetch-Site': 'same-site',
     'Pragma': 'no-cache',
     'Cache-Control': 'no-cache',
     # Requests doesn't support trailers
     # 'TE': 'trailers',
 }

params = {
     'user_goal': 'cbse',
     'user_exam': '12th cbse',
     'source': 'SEO Page ',
     'locale': 'en',
     'query': 'videos',
     'facet': 'videos',
     'start': '0',
     'size': '10',
 }

response = requests.get('https://api-prod-cf.embibe.com/fs_ms/v2/search', params=params, headers=headers)
js=response.json()
l=[]




try:
    while int(params["start"])<=js["results"][0]["no_of_results"]:
        response = requests.get('https://api-prod-cf.embibe.com/fs_ms/v2/search', params=params, headers=headers)
        js=response.json()
        cookie=(response.cookies["__cf_bm"])
        try:
            for i in js["results"][0]["content"]:
                link=i.get("url")
                l.append(link)
                # link=(i.get("url").split("/")[-1])
                # print(link)
                # crl=crawl(link,cookie)
                # print(crl)
            print(len(l))
        except:
            None
        params["start"]=str(int(params["start"])+int(params["size"]))
except:
     None

df=pd.DataFrame(l)
df.to_excel("flp.xlsx",index=False)


print()
    
