
import requests
import pandas as pd
cookies = {
    'V': '201',
    '_ga': 'GA1.2.1697803135.1713592012',
    '_gcl_au': '1.1.576042546.1713592013',
    'FirstPage': 'Fri Apr 26 2024 15:06:32 GMT+0530 (India Standard Time)',
    'AB': 'B',
    '_fbp': 'fb.1.1713592015296.550621301',
    '_fpuuid': 'qylD-nptK1-guFt87FmCn',
    'jioAdsFeatureVariant': 'true',
    '_scid': 'f403dd52-0586-48e8-b15b-c7b65db82bbd',
    'cdigiMrkt': 'utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3AMon%2C%2020%20May%202024%2009%3A36%3A32%20GMT%7C',
    '_sctr': '1%7C1713551400000',
    'g_state': '{"i_p":1713936607907,"i_l":2}',
    'cto_bundle': 'oo8M6l9wak5FeWRITSUyRmxwMERCdmRrRE5MQldFTGh6VkFwb3Y5djR6TjYlMkZaaHYzVnhIU2dhOTd6WEYlMkZld21qJTJCbHdIM1VNSVAwNzgyc0xlbTRWbHhFOVVDYm5BSWZZSTRBZkxvbktxQmRENWRYMTUlMkZUVEltRnFWdlVKQzk4T2NxQVpURVpQUVpNVzlFeEVFRDZsWHkxbHBseHB3JTNEJTNE',
    'TS01de1f4a': '01ef61aed0be82e197c2903eb481b53e2becab46c809b0b179fe97c032cf00a2f4127ec943f8464d34c32538347c4c4823d67bfa8e93ed06d64f32a21bd1146a137e47f87c063f554f21c50eb044c6a78134fc48d90f3fdb740c7b5d258a70496d69139018',
    'TS01ac9890': '01ef61aed0557f1ded02b3f6362c91690fcf08f6918132875861c0627ab630d5ef62a09c2a2d420d0d43cb40168da39f0146bb1dd5',
    'recentlyViewed': '[{"id":"466817674_white","store":0},{"id":"443015881_khaki","store":0},{"id":"467159861_mustard","store":0},{"id":"443005600_mediumblue","store":0}]',
    '_gid': 'GA1.2.743347577.1714124131',
    'sessionStatus': 'true|undefined',
    'ifa': 'a030d156-2b84-439c-bbdd-5825d9428e30',
    'os': '4',
    'vr': 'WEB-1.15.18',
    'ImpressionCookie': '0',
    '_scid_r': 'f403dd52-0586-48e8-b15b-c7b65db82bbd',
    '_dc_gtm_UA-68002030-1': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.ajio.com/men-shirts/c/830216013',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': 'V=201; _ga=GA1.2.1697803135.1713592012; _gcl_au=1.1.576042546.1713592013; FirstPage=Fri Apr 26 2024 15:06:32 GMT+0530 (India Standard Time); AB=B; _fbp=fb.1.1713592015296.550621301; _fpuuid=qylD-nptK1-guFt87FmCn; jioAdsFeatureVariant=true; _scid=f403dd52-0586-48e8-b15b-c7b65db82bbd; cdigiMrkt=utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3AMon%2C%2020%20May%202024%2009%3A36%3A32%20GMT%7C; _sctr=1%7C1713551400000; g_state={"i_p":1713936607907,"i_l":2}; cto_bundle=oo8M6l9wak5FeWRITSUyRmxwMERCdmRrRE5MQldFTGh6VkFwb3Y5djR6TjYlMkZaaHYzVnhIU2dhOTd6WEYlMkZld21qJTJCbHdIM1VNSVAwNzgyc0xlbTRWbHhFOVVDYm5BSWZZSTRBZkxvbktxQmRENWRYMTUlMkZUVEltRnFWdlVKQzk4T2NxQVpURVpQUVpNVzlFeEVFRDZsWHkxbHBseHB3JTNEJTNE; TS01de1f4a=01ef61aed0be82e197c2903eb481b53e2becab46c809b0b179fe97c032cf00a2f4127ec943f8464d34c32538347c4c4823d67bfa8e93ed06d64f32a21bd1146a137e47f87c063f554f21c50eb044c6a78134fc48d90f3fdb740c7b5d258a70496d69139018; TS01ac9890=01ef61aed0557f1ded02b3f6362c91690fcf08f6918132875861c0627ab630d5ef62a09c2a2d420d0d43cb40168da39f0146bb1dd5; recentlyViewed=[{"id":"466817674_white","store":0},{"id":"443015881_khaki","store":0},{"id":"467159861_mustard","store":0},{"id":"443005600_mediumblue","store":0}]; _gid=GA1.2.743347577.1714124131; sessionStatus=true|undefined; ifa=a030d156-2b84-439c-bbdd-5825d9428e30; os=4; vr=WEB-1.15.18; ImpressionCookie=0; _scid_r=f403dd52-0586-48e8-b15b-c7b65db82bbd; _dc_gtm_UA-68002030-1=1',
}

params = {
    'fields': 'SITE',
    'currentPage': '0',
    'pageSize': '45',
    'format': 'json',
    'query': ':relevance',
    'sortBy': 'relevance',
    'gridColumns': '3',
    'advfilter': 'true',
    'platform': 'Desktop',
    'showAdsOnNextPage': 'true',
    'is_ads_enable_plp': 'true',
    'displayRatings': 'true',
}


response = requests.get('https://www.ajio.com/api/category/830216013', params=params, cookies=cookies, headers=headers)

js=response.json()

start_page=js["pagination"]["currentPage"]
end_page=js["pagination"]["totalPages"]

data=[]

while start_page<=end_page:
    response = requests.get('https://www.ajio.com/api/category/830216013', params=params, cookies=cookies, headers=headers)
    js=response.json()

    for i in js["products"]:
        try:
            image_url=i["fnlColorVariantData"]["outfitPictureURL"]
        except:
            image_url="Not available"

        try:
            discount=i["discountPercent"]
        except:
            discount="Not available"

        try:
            price=i["price"]["displayformattedValue"]
        except:
            price="Not available"

        try:
            old_price=i["wasPriceData"]["displayformattedValue"]
        except:
            old_price="Not available"

        try:
            url="https://www.ajio.com"+i["url"]
        except:
            url="Not available"
            print(url)
        
        try:
            brand_name=i["fnlColorVariantData"]["brandName"]
        except:
            brand_name="Not available"

        try:
            rating=i["averageRating"]
        except:
            rating="Not available"
        

        try:
            name=i["name"]
        except:
            name="Not available"

        data.append({
            "BRAND_NAME":brand_name,
            "NAME":name,
            "RATING":rating,
            "PRICE":price,
            "OLD_PRICE":old_price,
            "DISCOUNT":discount,
            "URL":url,
            "IMAGE_URL":image_url
        })
    print(len(data)) 
    start_page+=1
    a=str(start_page)
    params["currentPage"]=a

df=pd.DataFrame(data)
df.to_excel("ajio.xlsx")
