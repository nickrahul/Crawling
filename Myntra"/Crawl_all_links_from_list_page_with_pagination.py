import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import time


cookies = {
    '_abck': '57EF76086319446CDC7409D7E4FCA019~0~YAAQpm0/F5gT3XyPAQAAk8QyigsMVZBXyo+9hy13fzFDlSNWmuzFdJaUVNejEnL7D+/jBsvlr4bd3UNyJARygRy/iyLwn7HC++qt/gx2HRDRE1T63b/ItYio9W5mWzg20cox1byLQlfEUPK359lQW6d+OiEC8lQSiwDdo3HxwApVB/tleZNrKmohsw2Q4+ePgOkotRiB/9ehthzT90vuxRq+TX0n1kSZ5uyImXxUsAJe+lILnedkWoEAkS7kMSEmAxV2OknHZtILKEroe1xcv7oPtmu+IjuPbZkdQsSyn9lUIg8JFVs5ygQl5UWC0+D70VSOMqTR6TOkme31KjqAvMJDGGehibul6oezMARvLAuyyXmaGpFSpYB8jyCBRfY5vMffAWKWSpUjmAW4QTIFlqAk/udh99a8EDDaMTGoRPWxfeuoeg==~-1~-1~-1',
    'mynt-eupv': '1',
    '_d_id': '9c4fb309-5bb4-4301-99df-3989d40c0e89',
    'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWldFMVpqUXdOekV0TUdJMk55MHhNV1ZtTFdJeU1ETXROMlZsWlRZNFpUVTFZalkySWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpBMU1qUTJOREVzSW1semN5STZJa2xFUlVFaWZRLjh1bEl4T0pXb1dGM3RqUUVHR2VpZE9aYWpKLVlVOFh3WDFzTWhEb3haRjQ=',
    'utrid': 'RWZlElAEEUtDW3dpAXBAMCMxNDAxNzQyNDgzJDI%3D.25b77528be15de2e79ff97b412d8f472',
    '_xsrf': 'mw7DN7jt8VqZkyOy2VzqdlYGPlQCXFB7',
    '_gcl_au': '1.1.87726560.1714972641',
    'mynt-ulc-api': 'pincode%3A226005',
    'mynt-loc-src': 'expiry%3A1716018530095%7Csource%3AIP',
    'x-mynt-pca': '7Vtjnk7mqGeGcRqXpzc7vhu8SJwop5I29e_O8a4i-6zkcjPHB1In0nwqxfFPGOPX3NCSo8RmwRvmNEKIYX1sMm_b5G4mbfaiuwbZ27mA_ZhBLgDIzk9SLJyCG320GJnuur0BQ2_xJyOrelpd4vmHFOcN08zMgSQ-3SapjKuT4B6g2whj3isC',
    'tvc_VID': '1',
    '_cs_ex': '1',
    '_cs_c': '1',
    '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D',
    '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22Thc2kT6SMxre0d1gMD1Y%22%7D',
    '_fbp': 'fb.1.1714972642459.1274784770',
    'cto_bundle': 'KUYt018wcVhIUmUlMkZpMU1scDB1RTdndk5QNE9BTjQ2N3JRNW9lQzI2YiUyRkZBJTJGTjFXYlB6YmVUamhkbkpkVnRBenN2M0FnRTU4WGo4ZXUlMkJTdnFYOGlyVUxwWkg2RzRCTXViMnglMkIxRUJEZVNaVFJERU1kWHFURzZCSVV3ZGpZeUVmYkVxZ0Y1d3Y1T0h2RFlrSnp5QnoxNnA5UyUyRkElM0QlM0Q',
    'lt_timeout': '1',
    'bm_sz': '1A9F8A0B5F59F79EF7E0EC0D62DA5736~YAAQdG0/Fwh2JG2PAQAAUxylihewarlMC9EFdIlANW0f80xYDFM5SvzOTXLZP4U0hyAgCjIwxJK47dQh0yzl9L0Lgc4xjLehU0mMp9aJCntXGIK+sct8vot7+Hk6nQr+DEleeWu46efZVI+Lq8zzlmUyx35pzhcyHHfQvhUpNvqTMbg6XoU7g4kUVfuHj/nIyYpWRWrDTg8GDuEEt/o5YRlaa/wGtWsPvWOo0fAW8vsy7F5tLpXJuGjQ2V4yWpFUUs8muz2O/wRIDizNOj+/2e5hPJyjRN8i2N5DQDr4f0UbA6LtBPnXoyLq2f3eZ78dFJMQy+KTVp/LNJ1vIxrd5fbtNCTOEKhUAcHI2xOa88fwrOvVBYqeemNPSIzs/NXAzPxdhlgbyukio5L3rSGhEHLKfJliZHRTZAvqq4GcYyTXFDZ8qoZlZ6HgyPQG97h9/y4XjkBJAGC7TWaw9PBtudJZJ4xqNctUI/OzMU+BeB2NthV7VHQCFx340+F0+riBG8y0JWDp3A1035rqOVVlU0wv+dywfD71N/8=~3420481~3749683',
    '_ma_session': '%7B%22id%22%3A%2209642a65-e393-4145-bdfb-1e050b5a8cce-9c4fb309-5bb4-4301-99df-3989d40c0e89%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D',
    'microsessid': '87',
    '_gcl_aw': 'GCL.1716010537.Cj0KCQjwgJyyBhCGARIsAK8LVLMZK_5aCK2PgBYWCdzUgVpcgLk_EObA2OJiTHEkIpPEs0xXyju6TPwaAhHDEALw_wcB',
    'ak_RT': '"z=1&dm=myntra.com&si=9bead7bf-580f-4a65-a9cf-820fa022b034&ss=lwbrbbjr&sl=h&tt=gme&obo=e&rl=1"',
    'AKA_A2': 'A',
    'dp': 'd',
    'user_session': 'I8wZ4fkbeovD_Yh_0hhO6g.F8RlPMmLXL1Wcl9CpSHZPbxAJM4IBqRw853avA9xtrwxMPinFePf1nGyXD05Rum_gWoGYQsJILWi7AZ8s9lKlCasAKXrnLO5WyDR9dO0LDKGChg2A3YealqFv6vMWozoMZcvri4Ki02Q8PvLs9NP-Q.1716017704382.86400000.gZYcJDNZr4hi_9yARIoiuv5_4AcdkfnYohr9TY9u1-o',
    'ak_bmsc': '1667D0A90DBF34E94DEB409F314BD297~000000000000000000000000000000~YAAQdG0/Fzx2JG2PAQAAXSyliheXmi/io/PRDKBbqX6cLyUqvGez/BWDXrqvrPIdH6mOWRX417+71NN9w/prLxpTzLt78FjiVq0cU5+wKZ/I1IaxWw6VFePp7x6vcvy/zfVfqGB8t/bCNWVF0Nzt8EqGq1SkALFw3K63YdB6ixmILrNuWUX+4m4MBSSOhkgYNj8C+MbmYSF24waRh2NfJ4cio6qkKOGpzmd5zziOemYIzfgSyrj+9qNEIus9HGbPH95oLY/h4/hIPoYkSGg30b2edPkGOp2+TGP8Aoss6yFiiepX33LrQ0nqOWI0j0ZU5+LZdb8mxyJdNqxMNB9vZSHVI+0UJ17urcamJ4UJ6QvL3anFRYSS7cxvXMgQNz5VWEJkFvecZCWIpPrGgevqdh0wy8BJn7kl4dWXOjPI+66y/as0XgWlMCDlCf4bF2q/lt8SS198PYFU63WMOaADlYRRh/UoKk4QdGh9F7yU9gJ/8//cPrcM',
    'bm_sv': '830A9C137E872F071C324DFD78DC1E43~YAAQdG0/F0B2JG2PAQAAki+lihd/ifwjc0JQw5T9xCVjzAYSQqX+wVnj94vTKy2mt7Hjgb+ZsxpA9eE2KHUxZpAumFACOnA2pgSiF9vRD5yAvWYG7S015qzJrCHiQAJeRIrvXV/XEMh0cWc02o4Rzqg5ddu35CnNwQEbVLlw3PxPyJGksIUDVgA2+gw8ieglnvN72hfSb9GX1z19D2YVEltGKpcNvcZH7/UJZFz/a2QhdmxnRU74QTR3vm5UTxfk~1',
    '_mxab_': 'config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bcoupon.cart.channelAware%3DchannelAware_Enabled',
    'lt_session': '1',
    'bm_mi': 'F59D1080969B7A821DD0FC2565AC5204~YAAQdG0/FwZ2JG2PAQAAUxylihcBF1kThJU/xU/e6aiP3oB96/eQewze4drKsVYoDp6SCix0v/YUges9GMH6S3M4rtdMtx9oICUW0e2PZgRziIKG1/AEqsMYu1yKUeHBaensIYm8rgJlqnp2QcfG5yqU74jHoEI1UpETtu4CsEAtgylv30LAdmAtzKNjOWNGxWbJndee/4xHNxPkOAyCyBuCGrttg+3+u4ruhqtO23W4JMtGu0jvrSbUdvGXU9khP6SoXsXhvdQmV6Hexdt7K8AP/gE5//xP/eY4eWq67NpZAb/pOJzP5rVroi0fMJ6QL3xTQ4bn~1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.myntra.com/men-tshirts',
    'X-myntraweb': 'Yes',
    'X-Requested-With': 'browser',
    'x-location-context': 'pincode=226005;source=IP',
    'x-meta-app': 'channel=web',
    'Content-Type': 'application/json',
    'app': 'web',
    'x-myntra-app': 'deviceID=9c4fb309-5bb4-4301-99df-3989d40c0e89;customerID=;reqChannel=web;appFamily=MyntraRetailWeb;',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': '_abck=57EF76086319446CDC7409D7E4FCA019~0~YAAQpm0/F5gT3XyPAQAAk8QyigsMVZBXyo+9hy13fzFDlSNWmuzFdJaUVNejEnL7D+/jBsvlr4bd3UNyJARygRy/iyLwn7HC++qt/gx2HRDRE1T63b/ItYio9W5mWzg20cox1byLQlfEUPK359lQW6d+OiEC8lQSiwDdo3HxwApVB/tleZNrKmohsw2Q4+ePgOkotRiB/9ehthzT90vuxRq+TX0n1kSZ5uyImXxUsAJe+lILnedkWoEAkS7kMSEmAxV2OknHZtILKEroe1xcv7oPtmu+IjuPbZkdQsSyn9lUIg8JFVs5ygQl5UWC0+D70VSOMqTR6TOkme31KjqAvMJDGGehibul6oezMARvLAuyyXmaGpFSpYB8jyCBRfY5vMffAWKWSpUjmAW4QTIFlqAk/udh99a8EDDaMTGoRPWxfeuoeg==~-1~-1~-1; mynt-eupv=1; _d_id=9c4fb309-5bb4-4301-99df-3989d40c0e89; at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWldFMVpqUXdOekV0TUdJMk55MHhNV1ZtTFdJeU1ETXROMlZsWlRZNFpUVTFZalkySWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTXpBMU1qUTJOREVzSW1semN5STZJa2xFUlVFaWZRLjh1bEl4T0pXb1dGM3RqUUVHR2VpZE9aYWpKLVlVOFh3WDFzTWhEb3haRjQ=; utrid=FVkKTX5QB0JDXWIIHgFAMCMyMDIyMzQ5MTAwJDI%3D.eae3caf3a791680746c6ef49d793a778; _xsrf=oWDSPeqlsaGsLFlXyLF2Fdd82PYQ20yj; _gcl_au=1.1.87726560.1714972641; mynt-ulc-api=pincode%3A226005; mynt-loc-src=expiry%3A1716011976226%7Csource%3AIP; x-mynt-pca=7Vtjnk7mqGeGcRqXpzc7vhu8SJwop5I29e_O8a4i-6zkcjPHB1In0nwqxfFPGOPX3NCSo8RmwRvmNEKIYX1sMm_b5G4mbfaiuwbZ27mA_ZhBLgDIzk9SLJyCG320GJnuur0BQ2_xJyOrelpd4vmHFOcN08zMgSQ-3SapjKuT4B6g2whj3isC; tvc_VID=1; _cs_ex=1; _cs_c=1; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22Thc2kT6SMxre0d1gMD1Y%22%7D; _fbp=fb.1.1714972642459.1274784770; cto_bundle=F_E8Pl8wcVhIUmUlMkZpMU1scDB1RTdndk5QNE5Pa0psMmowdSUyQnByQ2lWdCUyRjU1ajR2JTJCQVFhMEpQNEdKNllKN0RGNTZRNUhFRk12aEdrd09HSWdaZkduTWpxRE93MmN6enlzT1MlMkZ5VlMyV3M0RnNDd0x1M0d1SEY2dUJkJTJGNElVSFNEOXlxS0w2TDlVejBrS0V4cyUyRiUyQnJUa2t1c0tBJTNEJTNE; _mxab_=config.bucket%3Dregular%3BConvenience_fee_logged_out_user%3Denabled%3Bcoupon.cart.channelAware%3DchannelAware_Enabled; _pv=default; dp=d; lt_timeout=1; lt_session=1; AKA_A2=A; ak_bmsc=74C5D1F2AAD7672FE55CFD74301B947B~000000000000000000000000000000~YAAQpm0/F+oT3XyPAQAA5tgyihdm4jHxFBuS+z1aQvB42FvDexAgjMZCq4MqH9VRWmYClHBs4zYYJjFwr5plhutWLVxHDCUG7tW0DIq1vXyJs9ZYYpHweQnqdCt1v6REmXJfQLb+tOKMrPlRj/c/HNV5Otvt+bOGDb0vUcEbwArmQyqLA16KSkeltU5uRnVE3XtucqDka85zCD/eu3eHf52Ewwt9xlQ++rn4xVddZ2v7eOPaUvq0rHHL//6lFHQCrgZaHEflIzAExXHNM/VlWUNIL0OQ9m2BbSOH0VZTW+hzO5QQZwadGcg5QdhY5mac+d35kaMkxRM3QsBZMtx+QIg1v0QmyNAlTyI81XAsn68/4xVwbNnHNoSSjkImKxHQ+JVEKhRsOiPh8vWYw57pF/LcqQZZ+jE6w2OlkaNCOI/sgMTJKDSChV5IvWbee63gOTaotcrpEFnzq4Sw7w589kOCViyV4bCl1NLxWkyu/rndhzFWss0H8Dpjrel0Lb/zb54yDoKrG98P+4fWq7788yfF0xb88qbaXW3aWVtOM73qMM1wJUWN5gM=; bm_sz=1A9F8A0B5F59F79EF7E0EC0D62DA5736~YAAQvQVaaIqgHoSPAQAAOZI2ihc8MB07uaztHSzBSFdJEDtB54KmJjZBxpnL2jVSvDmyhZ6FUY61a5fRAuX5AVrD1d5NwIYdyADgLBA/eO5V8F1STGVpv+EPMmfXAIiJJykpk86lwIdQg+xc5Z9fG/+apCXQA86hHWtE2dBX9hLcH65YQN5F3aAgVIvmPHsy+BlmJhq3H2D2SMMdlykjVrgu2hx34vTFDMjGMngemSNtAvp7qJYa5jT52bIH5twIS432D805ecvmeiEFsJGKDoGdf+6oYkp+aZt7dJYgGRsCgK3kX+5Y1wyqtnFpAlJQj/AELJzOyo2TsoBB6f1xGQ0ytUTyucHHR/bZuGyS3RFGz0yp1Vx7ZtHKDZDwUhPHXlTsNx4GSoKxOIb9CSseWDrYvm7q9UgGg0rmBaBlDsKwx51oeqeEV981zPIq1Jxa+vlz~3420481~3749683; _ma_session=%7B%22id%22%3A%2209642a65-e393-4145-bdfb-1e050b5a8cce-9c4fb309-5bb4-4301-99df-3989d40c0e89%22%2C%22referrer_url%22%3A%22https%3A%2F%2Fwww.myntra.com%2Fshop%2Fmen%22%2C%22utm_medium%22%3A%22searchbrand_cpc%22%2C%22utm_source%22%3A%22dms_google%22%2C%22utm_channel%22%3A%22other%22%7D; bm_sv=6DF6B3068351782D5D82F051C7E72E4C~YAAQvQVaaMagHoSPAQAASpk2ihezLqZlD6Z1XDDKkcaWvaAJ5OyhjXPchbOaQcwxlkQnI/hgqNY+wNj6Nmx/QvN3zSdfAD7zE54rc1s8rAkfNbxJW5GP2imXayadSxxn7dUkipVFnjQW7bWpzDBOaJO7UV5MZdap3zII9M6YzAyxhcaj0VF+u36wG/OtZq8ZyUDYYmhV69KadgLBDQZ3D+VtlL+gNhfZdeUTWdxmxfZnz9kxaYyS4LRf0rQbQSq69A==~1; microsessid=87; user_session=bhtUwiRFztCcS3aX_WPjlw.PEY0hhBCXgJQK35JYfq6YX5OSl1pjXEgcNoCMWZVY69L-wt6bORxwYGY4v6kg54v-AlkOsCJOtAnCf6KNPJzgtnYiQVbyj_0imbPrfokhYg6DHg8sMXUQ6OvDJWh19euDkdAi5vsykIPqdEA_Fq9hQ.1716010534726.86400000.REvuK6Yczd6TTNVFKwgSbS7y5MN9KHi2bMbU2cx1F6A; _gcl_aw=GCL.1716010537.Cj0KCQjwgJyyBhCGARIsAK8LVLMZK_5aCK2PgBYWCdzUgVpcgLk_EObA2OJiTHEkIpPEs0xXyju6TPwaAhHDEALw_wcB; ak_RT="z=1&dm=myntra.com&si=9bead7bf-580f-4a65-a9cf-820fa022b034&ss=lwbod6dr&sl=5&tt=6j3&obo=3&rl=1&nu=2xmttkra&cl=6dwx&ld=6dzz&r=2xmttkra&ul=6e00"; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1716010783%2C%22trackend%22%3A1716010843%7D',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'rows': '50',
    'o': '0',
    'plaEnabled': 'false',
    'xdEnabled': 'false',
    'pincode': '226005',
}




class Crawl:
    def __init__(self,url) -> None:
        response = requests.get(url, params=params, cookies=cookies, headers=headers)
        if response.status_code==200:
            js=response.json()
            self.list_page(js)

    def list_page(self,js):
        links=[]
        a=1
        t=0
        try:
            while len(links)!=js["totalCount"]:
                response = requests.get(url, params=params, cookies=cookies, headers=headers)
                js=response.json()
                if js["products"]:
                    for i in js["products"]:
                        links.append("https://www.myntra.com/"+i.get("landingPageUrl"))
                time.sleep(10)
                print(len(links))
                a+=1
                headers["Referer"]=f'https://www.myntra.com/men-tshirts?p={a}'
                params["p"]=a
                if int(params["o"])==0:
                    t+=49
                else:
                    t+=50

                params["o"]=str(t)
        except:
            None
        df=pd.DataFrame(links)
        df.to_excel("myntra.xlsx",index=False)



url='https://www.myntra.com/gateway/v2/search/men-tshirts'
crl=Crawl(url)
