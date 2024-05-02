import requests
from bs4 import BeautifulSoup as BS


cookies = {
    'session-id': '261-5318867-9385605',
    'i18n-prefs': 'INR',
    'ubid-acbin': '260-2326724-7002715',
    'session-id-time': '2082787201l',
    'session-token': 'Sjkfg7Ag1RUw+Laat7f6IJgpTXgEE30ZC3Z5KbH36rWe/8Vyct4Ah0+J7LQCPIO33IUN1qFq6lRITwOERyE6NG0NYItyrFmUn8kRcXTQFlaVXtcQcvdNImzxyWL5LeX3ZnpmmhsPmD9kVp+399WvT/jYbMWE3PtrgUvWEqK6woil50BWFAwPBhP7jiyeGHIwZWh3Te4VV9RfBHTuLNZZ9jWr41AxwsnbUwlFx6SI1N2aoMXl/6vgl79yArtcRB+cMjhLzG19ES2Bb6N4kiRC8dWG1reVH2QUCVsuEHeDGJX4CH2PrIdasBAUph7TcQBuRebHFetKpnB5cFNkHZatUzd5PELhuS1n',
    'csm-hit': 'tb:3XPC4CYY0MS8QN8BRQSE+s-HMZJWJM5QB6MM2JZWR9M|1714300200229&t:1714300200229&adb:adblk_no',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,mr;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'session-id=261-5318867-9385605; i18n-prefs=INR; ubid-acbin=260-2326724-7002715; session-id-time=2082787201l; session-token=Sjkfg7Ag1RUw+Laat7f6IJgpTXgEE30ZC3Z5KbH36rWe/8Vyct4Ah0+J7LQCPIO33IUN1qFq6lRITwOERyE6NG0NYItyrFmUn8kRcXTQFlaVXtcQcvdNImzxyWL5LeX3ZnpmmhsPmD9kVp+399WvT/jYbMWE3PtrgUvWEqK6woil50BWFAwPBhP7jiyeGHIwZWh3Te4VV9RfBHTuLNZZ9jWr41AxwsnbUwlFx6SI1N2aoMXl/6vgl79yArtcRB+cMjhLzG19ES2Bb6N4kiRC8dWG1reVH2QUCVsuEHeDGJX4CH2PrIdasBAUph7TcQBuRebHFetKpnB5cFNkHZatUzd5PELhuS1n; csm-hit=tb:3XPC4CYY0MS8QN8BRQSE+s-HMZJWJM5QB6MM2JZWR9M|1714300200229&t:1714300200229&adb:adblk_no',
    'device-memory': '4',
    'downlink': '10',
    'dpr': '0.8333333333333333',
    'ect': '4g',
    'priority': 'u=0, i',
    'referer': 'https://www.amazon.in/',
    'rtt': '200',
    'sec-ch-device-memory': '4',
    'sec-ch-dpr': '0.8333333333333333',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-viewport-width': '1484',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'viewport-width': '1484',
}

params = {
    'k': 'iphone',
    'crid': '22MXUOY7Z3LQ3',
    'sprefix': 'iphon,aps,274',
    'ref': 'nb_sb_noss_2',
}

username = "ua64eb42a570005c7-zone-custom"
password = "ua64eb42a570005c7"
PROXY_DNS = "43.152.113.55:2334"
proxy = {"http":"http://{}:{}@{}".format(username, password, PROXY_DNS)}



class Crawl:
    def __init__(self,url) -> None:
        self.url=url
        response = requests.get(url, params=params, cookies=cookies, headers=headers,proxies=proxy)
        if response.status_code==200:
            self.list_page(url)
        else:
            print("response not valid")

    def list_page(self,url):
        a=url
        self.data=[]
        while True:
            r=requests.get(a, params=params, cookies=cookies, headers=headers,proxies=proxy)
            soup=BS(r.content,"html.parser")
            for i in soup.find_all("div","puisg-col puisg-col-4-of-12 puisg-col-4-of-16 puisg-col-4-of-20 puisg-col-4-of-24 puis-list-col-left"):
                links=("https://www.amazon.in"+i.find("a").get("href"))
                self.detail_page(links)
            try:
                if soup.find("a","s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"):
                    a="https://www.amazon.in"+("a","s-pagination-item s-pagination-next s-pagination-button s-pagination-separator").get("href")
                    print(a)
                else:
                    break
            except:
                print("nahi mila")


    def detail_page(self,links):
        r1=requests.get(links, params=params, cookies=cookies, headers=headers,proxies=proxy)
        print(r1,"------------------------------------------------------------------------------------------")
        soup1=BS(r1.content,"html.parser")
        try:
            title=soup1.find("div",id="titleSection").find("h1").text.strip()
        except:
            title="Not available"

        try:
            rating=soup1.find("span",id="acrPopover").text.strip()[0:3]
        except:
            rating="Not available"

        try:
            discount=soup1.find("span","a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage").text
        except:
            discount="Not available"

        try:
            price=soup1.find("span","a-price-whole").text
        except:
            price="Not available"

        try:
            mrp_price=soup1.find("span","a-size-small aok-offscreen").text.strip()
        except:
            mrp_price="Not available"

        try:
            colors=[]
            for j in soup1.find("ul","a-unordered-list a-nostyle a-button-list a-declarative a-button-toggle-group a-horizontal a-spacing-top-micro swatches swatchesSquare imageSwatches").find_all("li"):
                colors.append(j.find("img").get("alt"))
        except:
            colors="Not available"

        try:
            variants=[]
            for i in soup1.find("ul","a-unordered-list a-nostyle a-button-list a-declarative a-button-toggle-group a-horizontal a-spacing-top-micro swatches swatchesSquare").find_all("li"):
                variants.append(i.find("p","a-text-left a-size-base").text)
        except:
            variants="Not available"

        try:
            images=[]
            for k in soup1.find("ul","a-unordered-list a-nostyle a-button-list a-vertical a-spacing-top-extra-large gridAltImageViewLayoutIn1x7").find_all("li"):
                if k.find("img"):
                    if k.find("input","a-button-input").find("img").get("src")[-3:]=="jpg":
                        images.append(k.find("input","a-button-input").find("img").get("src"))
        except:
            images="Not available"

        self.data.append({
            "TITLE":title,
            "RATING":rating,
            "DISCOUNT":discount,
            "PRICE":price,
            "MPR_PRICE":mrp_price,
            "COLORS":colors,
            "VARIANTS":variants,
            "IMAGES":images
        })
        print(self.data)
       

url="https://www.amazon.in/s"
crl=Crawl(url)
