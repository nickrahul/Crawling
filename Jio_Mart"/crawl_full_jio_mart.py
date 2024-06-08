import re
from bs4 import BeautifulSoup as BS
import pandas as pd
import time
import  html


import requests

cookies = {
    'AKA_A2': 'A',
    'ajs_anonymous_id': 'e33b0798-cc22-411d-ac9f-0f21a78c8578',
    'nms_mgo_pincode': '400020',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.8',
    # 'cookie': 'AKA_A2=A; ajs_anonymous_id=e33b0798-cc22-411d-ac9f-0f21a78c8578; nms_mgo_pincode=400020',
    'pin': '400020',
    'priority': 'u=1, i',
    'referer': 'https://www.jiomart.com/',
    'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}




class Crawl:
    def __init__(self,url):
        self.dat=[]
        response = requests.get(url, cookies=cookies, headers=headers)
        if response.status_code==200:
            js=response.json()
            self.main_page(js)
            df=pd.DataFrame(self.dat)
            df.to_excel("jiomart.xlsx",index=False)

    
    def main_page(self,js):
        data=js["data"]
        for i in range(0,8):
            names=(data[i].get("name"))
            for j in (data[i]["sub_categories"]):
                subnames=(j.get("name"))
                for k in (j.get("sub_categories")):
                    links="https://www.jiomart.com/"+(k.get("url_path"))
                    self.list_page(links)
            break
            


    def list_page(self,links):
        ab=links.split("/")[-1]
        ba=0
        while True:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'https://www.jiomart.com/',
                'x-algolia-api-key': 'aace3f18430a49e185d2c1111602e4b1',
                'x-algolia-application-id': '3YP0HP3WSH',
                'Origin': 'https://www.jiomart.com',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
            }

            data_part1 = '{"requests":[{"indexName":"prod_mart_groceries_products_popularity","params":"attributesToHighlight=%5B%5D&attributesToRetrieve=%5B%22*%22%2C%22-algolia_facet%22%2C%22-alt_class_keywords%22%2C%22-available_stores%22%2C%22-avg_discount%22%2C%22-avg_discount_pct%22%2C%22-avg_discount_rate%22%2C%22-avg_mrp%22%2C%22-avg_selling_price%22%2C%22-search_keywords%22%5D&clickAnalytics=true&enableRules=true&facets=%5B%22algolia_facet.*%22%2C%22avg_discount_pct%22%2C%22avg_selling_price%22%2C%22brand%22%2C%22category_level.level4%22%5D&filters=category_ids%3A'
            data_part2 = f'{ab}'
            data_part3 = '%20AND%20availability_status%3AA%20%20AND%20(mart_availability%3AJIO%20OR%20mart_availability%3AJIO_INSTA%20OR%20mart_availability%3AJIO_WA%20OR%20mart_availability%3AJIO_INSTA_WA)%20AND%20(buybox_mrp.6217.available%3Atrue%20OR%20buybox_mrp.PANINDIAGROCERIES.available%3Atrue%20OR%20buybox_mrp.S575.available%3Atrue)%20AND%20(available_stores%3A6217%20OR%20available_stores%3APANINDIAGROCERIES%20OR%20available_stores%3AS575)%20AND%20((inventory_stores%3AALL%20OR%20inventory_stores%3Agroceries_zone_non-essential_services%20OR%20inventory_stores%3Ageneral_zone%20OR%20inventory_stores%3Agroceries_zone_essential_services%20OR%20inventory_stores%3ATMW6%20OR%20inventory_stores%3AS575%20OR%20inventory_stores_3p%3AALL%20OR%20inventory_stores_3p%3Agroceries_zone_non-essential_services%20OR%20inventory_stores_3p%3Ageneral_zone%20OR%20inventory_stores_3p%3Agroceries_zone_essential_services%20OR%20inventory_stores_3p%3ATMW6%20OR%20inventory_stores_3p%3AS575))&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&hitsPerPage=12&maxValuesPerFacet=50&page='
            data4=f"{ba}"
            data5='&query=&ruleContexts=%5B%22PLP%22%5D&tagFilters="}]}'

            data = data_part1 + data_part2 + data_part3 + data4 + data5

            response = requests.post(
                'https://3yp0hp3wsh-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.5.1)%3B%20Browser%3B%20instantsearch.js%20(4.59.0)%3B%20JS%20Helper%20(3.15.0)',headers=headers,data=data,)
            js=response.json()
            
            for i in js["results"][0]["hits"]:
                linkk=("https://www.jiomart.com"+i.get("url_path"))
                self.detail_page(linkk)
            ba+=1
            if ba==js["results"][0]["nbPages"]:
                break
        
    
    def detail_page(self,linkk):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': f'{linkk}',
            'pin': '400020',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Connection': 'keep-alive',
            # 'Cookie': '_ALGOLIA=anonymous-92a4fa30-b082-427c-8546-82f66dabb433; nms_mgo_city=Mumbai; nms_mgo_state_code=MH; WZRK_G=55906665b38e449880392e4660bde1f0; _ga_XHR9Q2M3VV=GS1.1.1717796994.9.1.1717798542.33.0.0; _ga=GA1.2.358288944.1717437762; _gac_UA-163452169-1=1.1717745467.CjwKCAjw34qzBhBmEiwAOUQcFy7xjio0sEg1cIyNF1hr6Kw5uYJN3_oHkGazS0QvHGFIbc6wyAEZORoCKfYQAvD_BwE; ajs_anonymous_id=c5b1c010-f0d7-4512-9e52-d38e72027ae6; RT="z=1&dm=www.jiomart.com&si=2c0cc4c8-a314-4271-9632-5f2df9c902cb&ss=lx580pjo&sl=3&tt=9qh&obo=2&rl=1"; _fbp=fb.1.1717437762874.1440177415; nms_mgo_pincode=400020; _gid=GA1.2.1395162911.1717577626; _gcl_aw=GCL.1717745467.CjwKCAjw34qzBhBmEiwAOUQcFy7xjio0sEg1cIyNF1hr6Kw5uYJN3_oHkGazS0QvHGFIbc6wyAEZORoCKfYQAvD_BwE; _gcl_gs=2.1.k1$i1717745463; AKA_A2=A; WZRK_S_88R-W4Z-495Z=%7B%22p%22%3A5%2C%22s%22%3A1717796997%2C%22t%22%3A1717798546%7D; _gat_UA-163452169-1=1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }
        a=linkk.split("/")[-1]
        response = requests.get(f'https://www.jiomart.com/catalog/productdetails/get/{a}', cookies=cookies, headers=headers)
        js=response.json()
        try:
            product_name=js["data"]["gtm_details"]["name"]
        except:
            product_name=None

        try:
            mrp=js["data"]["gtm_details"]["price"]
        except:
            mrp=None

        try:
            image_url="https://www.jiomart.com"+js["data"]["image_url"]
        except:
            image_url=None

        try:
            response1 = requests.get(f'https://www.jiomart.com/catalog/reviewwidget/{a}',headers=headers)
            js1=response1.json()
            average_rating=js1["data"]["data"]["averageRating"]
            
        except:
            average_rating=None

        try:
            ratings_count=js1["data"]["data"]["ratingsCount"]     
        except:
            ratings_count=None

        d={}
        d.update({"PRODUC_NAME":product_name,"MRP":mrp,"IMAGE_URL":image_url,"AVERAGE_RATING":average_rating,"RATINGS_COUNT":ratings_count,"LINK":linkk})
        self.dat.append(d)
        print(len(self.dat))





    


url='https://www.jiomart.com/catalog/tree_json_plp/algolia'
crl=Crawl(url)



