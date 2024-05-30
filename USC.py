
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd


cookies = {
    'segment_anonymous_id': '9af0c6d9-5d92-49b7-ad8d-0e964cd50240',
    'X-SD-URep': '69fe8ea7-7bfd-4b50-a59f-ae83185ca42a',
    'usc_AuthenticationCookie': '9af0c6d9-5d92-49b7-ad8d-0e964cd50240',
    'TS01f2aabf': '01e4dc9a763b65f1212dde3a9b4e1c273c0d12a513eb000d753e7da7f2946be9a290ccd1fee84748b5c78db6fbbc1e51ebc9ed0d53a42f3c03c5ed74fad5ce3e56996a4071d247a28aa0b064c53821617ecbae636992995e35bb2914b0a55bab47f189a847774fff981419f32fd6797ad5ea7ad10426f67ae495b2c03070ce9052ce1dde38',
    '_abck': '9C46DFC76144C89F9F14611BB3F188BF~0~YAAQ1m0/F+L1MciPAQAA5zXNyAt/EX/vixDzDc/E71lEjast9Xw2tp1lP/WPIP2uEjjcyxHPW19qUiBsRYl7fqws66asi0wcXD8xJ5PzEftS9iI1fMWEqu1WJJNYsFohmUKBiRjks/6Z3QRC4FTZbpmSyxFDai9TLeYDbq9d/Ajyauxf3T0FfbbLu+P+oX3QXaYKTbU97goNFYtwhJ7JGVQQDTSM8nAFsZiz5euwhlxaZIlD7m1FhDfAu1ctVkE45JluUYktfI0RPuedZXchrb/KpiKt2ToCs64pFxYsLcF4t5HQ8TsqVic7UZFGwx2wAyLQNOw2YuRXMeyNVKgR+6nwMUYFjVWBmBpdU7Y1jtHdyMBDq1lydH+TjqrZ4zZSZy+EZ2CrUdbW7La+na8G6a6ZufHCbSXXHinvxlpyX2Mp5vK5~-1~||0||~1717064442',
    'ak_bmsc': 'DBFB10D85B1D7E7696F39FE472910D95~000000000000000000000000000000~YAAQ1m0/F+P1MciPAQAANDbNyBdCV7MgBc0u4vuKobDlkUAeh+1Uqp7OyGZOzzmvAiEermr55tP9q4zoewfrfW820s01tHxKxSBeOeZRzWwhLlcvSq0n5s3n44KM11tGQJadbpgW7x3ATLGSYFkdXv5X5ekb9a2t5sFoNz8VWZum5ekhPXe2OI4LYXXgP/3+FPa4DjsXFnxW12CaF53CcW/lrQjjO2o6+9EbilHaae6CVMhp/XFrTAusiLMv+vQdqlYVzpSOKbYp+N6j0ODWGYYE58JaAM3EmRmYfGXJxl2sFEMEe04v64p6qLgFeqljyu4sxVx+6110d7Cf+s2Y5s5rtLQPmgQtj+F4uJohV+AK1ymI6pvwXLW3TUYNsPND4t0h48Ko8NpJbpJaiJLxJ8JfKczeA+Jw6SuXxQ4kcl3affl+IdS7E69fVfpCYdQo1aBqOZo6zVj4wvuA3ouJtCfMbX3ePHQEfK4jG0cU7od48xzKSg==',
    'bm_sz': '837A180724415D01D3D6C70593FFDB2B~YAAQx20/FziisriPAQAACqzUyBcr5FlEYa+6iLr+hWTqUFP4Ueq73OY73QAOzfcUXGLIP6xAD4fDlZWYg8mdwHwmylANvyYbCC4hjbvEX07ebpgz2klQe9asVfF85xwDdC4fvgdBKr8Ih6LnjhvSep3DbzhgFqNL+lE4AiyZlGChmg29rahHkmhXArRjvD1LuSPNP7zN2wS+OrT/1wKMMcPFsjXmyxaeiNeLsQ+YQCsbHUHzvlrMicQ9EPur3Isr7MSvMOviTGziBReFooGwGk+ubY/slEWBPvO83Soo4P43svcVBDiHV5wg9CphVsvPrhm+OUljHqStIUbEKzzX5iEWJOxSKOANhZI/bURmOWDP/jg6D5IyYCaC2aDnqy3oWtsD9064zZsTKCYxaIVp8hampfEZDdOchUSNRljc/KyXEgFsh30q7Y4DOsI5CCamhWA27EWvgPSuf/rL4nLb8/KtJ6wha1ET7+3WOdOSbCrJgk2WCR354uCNGTuMT8RVEVDMgCW3jNktr0a6iSY0EJ0B2ribw2UOjP149rgd6M8XJg==~4277555~3617587',
    'selectedLevel2MenuTabId': '0',
    'bm_sv': '01103FCD08CC725654B774795CBC2AC4~YAAQx20/FzeisriPAQAACqzUyBeOotiA6jQtDoyOySinxPphT44B4UYuuY1r5ivJPZecbmcBMVQPvwxi2sR57WRjopZoIRA8l9l2ortaoIsTYOmetXyoXfwIoDm4iB04ZP/4VWlq5Hcmq3412VhPo1qx40tfvCWcF5djEpnXShFX7e6MLkjfLgFym1WEtOJJo9TAlfcTdnrRpjv1Yp4cIDdaTBDeWnVAe8u7/RfiIBK8Rj4JSQ6elHtblDMEEfq3~1',
    '_ALGOLIA': 'anonymous-0d5361e2-bb11-469f-b7aa-15272d569358',
    'dtCookie': 'v_4_srv_8_sn_2OSBROA0MJ8UHSPIF6RAI7SHA3NLFC5U_app-3Ab9702d2cec8810b9_1_ol_0_perc_100000_mul_1',
    'rxVisitor': '17170608451271NU585H95JA5441Q0H00TIQ0UOOJ6K6T',
    'dtPC': '8$461372412_793h-vLRPKJGFIUHFUOQUBQJRFUHMLAGACWJEQ-0e0',
    'rxvt': '1717063172419|1717060845127',
    'dtSa': '-',
    '_cq_duid': '1.1717060845.cmM1U5CEsrkc0Kd9',
    '_cq_suid': '1.1717060845.KyfnMH1zjtLhB4cV',
    '_cs_c': '0',
    '_cs_id': 'f770cb71-8f6a-a653-cfc1-50e2bf43f337.1717060845.1.1717061373.1717060845.1.1751224845863.1',
    '_cs_s': '34.0.0.1717063173663',
    'scarab.visitor': '%2241422F7BB79A40B7%22',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+May+30+2024+14%3A59%3A32+GMT%2B0530+(India+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f61812e4-c79f-4237-abac-5e45868b86f9&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IN%3BDL&AwaitingReconsent=false',
    'ajs_anonymous_id': '9af0c6d9-5d92-49b7-ad8d-0e964cd50240',
    'OptanonAlertBoxClosed': '2024-05-30T09:20:51.885Z',
    '_gcl_au': '1.1.2121841055.1717060852',
    '_ga': 'GA1.1.1187245688.1717060846',
    '_gid': 'GA1.3.807000556.1717060852',
    '_ga_VXFM372VJS': 'GS1.1.1717060845.1.1.1717061373.19.0.0',
    '_ga_E9W6WKDZGY': 'GS1.3.1717060853.1.1.1717061373.21.0.0',
    '_fbp': 'fb.2.1717060854326.699607901',
    'optimizelyEndUserId': 'oeu1717060854442r0.05671052278358091',
    'peerius_sess': '155891545517|3WiR-5A4OOB_5Hg6fQTagiJ-oyKD-xnBCl3dg56k3BA',
    'peerius_user': 'cuid:121743354067|KxYdvQ7u1o1evxkRAW1xemb78wzNgoLoKUyvD0zNnm4',
    'segment_anonymous_id': '9af0c6d9-5d92-49b7-ad8d-0e964cd50240',
    '_gat_UA-2579437-22': '1',
    '_dc_gtm_UA-2579437-22': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    # 'Cookie': 'segment_anonymous_id=9af0c6d9-5d92-49b7-ad8d-0e964cd50240; X-SD-URep=69fe8ea7-7bfd-4b50-a59f-ae83185ca42a; usc_AuthenticationCookie=9af0c6d9-5d92-49b7-ad8d-0e964cd50240; TS01f2aabf=01e4dc9a763b65f1212dde3a9b4e1c273c0d12a513eb000d753e7da7f2946be9a290ccd1fee84748b5c78db6fbbc1e51ebc9ed0d53a42f3c03c5ed74fad5ce3e56996a4071d247a28aa0b064c53821617ecbae636992995e35bb2914b0a55bab47f189a847774fff981419f32fd6797ad5ea7ad10426f67ae495b2c03070ce9052ce1dde38; _abck=9C46DFC76144C89F9F14611BB3F188BF~0~YAAQ1m0/F+L1MciPAQAA5zXNyAt/EX/vixDzDc/E71lEjast9Xw2tp1lP/WPIP2uEjjcyxHPW19qUiBsRYl7fqws66asi0wcXD8xJ5PzEftS9iI1fMWEqu1WJJNYsFohmUKBiRjks/6Z3QRC4FTZbpmSyxFDai9TLeYDbq9d/Ajyauxf3T0FfbbLu+P+oX3QXaYKTbU97goNFYtwhJ7JGVQQDTSM8nAFsZiz5euwhlxaZIlD7m1FhDfAu1ctVkE45JluUYktfI0RPuedZXchrb/KpiKt2ToCs64pFxYsLcF4t5HQ8TsqVic7UZFGwx2wAyLQNOw2YuRXMeyNVKgR+6nwMUYFjVWBmBpdU7Y1jtHdyMBDq1lydH+TjqrZ4zZSZy+EZ2CrUdbW7La+na8G6a6ZufHCbSXXHinvxlpyX2Mp5vK5~-1~||0||~1717064442; ak_bmsc=DBFB10D85B1D7E7696F39FE472910D95~000000000000000000000000000000~YAAQ1m0/F+P1MciPAQAANDbNyBdCV7MgBc0u4vuKobDlkUAeh+1Uqp7OyGZOzzmvAiEermr55tP9q4zoewfrfW820s01tHxKxSBeOeZRzWwhLlcvSq0n5s3n44KM11tGQJadbpgW7x3ATLGSYFkdXv5X5ekb9a2t5sFoNz8VWZum5ekhPXe2OI4LYXXgP/3+FPa4DjsXFnxW12CaF53CcW/lrQjjO2o6+9EbilHaae6CVMhp/XFrTAusiLMv+vQdqlYVzpSOKbYp+N6j0ODWGYYE58JaAM3EmRmYfGXJxl2sFEMEe04v64p6qLgFeqljyu4sxVx+6110d7Cf+s2Y5s5rtLQPmgQtj+F4uJohV+AK1ymI6pvwXLW3TUYNsPND4t0h48Ko8NpJbpJaiJLxJ8JfKczeA+Jw6SuXxQ4kcl3affl+IdS7E69fVfpCYdQo1aBqOZo6zVj4wvuA3ouJtCfMbX3ePHQEfK4jG0cU7od48xzKSg==; bm_sz=837A180724415D01D3D6C70593FFDB2B~YAAQx20/FziisriPAQAACqzUyBcr5FlEYa+6iLr+hWTqUFP4Ueq73OY73QAOzfcUXGLIP6xAD4fDlZWYg8mdwHwmylANvyYbCC4hjbvEX07ebpgz2klQe9asVfF85xwDdC4fvgdBKr8Ih6LnjhvSep3DbzhgFqNL+lE4AiyZlGChmg29rahHkmhXArRjvD1LuSPNP7zN2wS+OrT/1wKMMcPFsjXmyxaeiNeLsQ+YQCsbHUHzvlrMicQ9EPur3Isr7MSvMOviTGziBReFooGwGk+ubY/slEWBPvO83Soo4P43svcVBDiHV5wg9CphVsvPrhm+OUljHqStIUbEKzzX5iEWJOxSKOANhZI/bURmOWDP/jg6D5IyYCaC2aDnqy3oWtsD9064zZsTKCYxaIVp8hampfEZDdOchUSNRljc/KyXEgFsh30q7Y4DOsI5CCamhWA27EWvgPSuf/rL4nLb8/KtJ6wha1ET7+3WOdOSbCrJgk2WCR354uCNGTuMT8RVEVDMgCW3jNktr0a6iSY0EJ0B2ribw2UOjP149rgd6M8XJg==~4277555~3617587; selectedLevel2MenuTabId=0; bm_sv=01103FCD08CC725654B774795CBC2AC4~YAAQx20/FzeisriPAQAACqzUyBeOotiA6jQtDoyOySinxPphT44B4UYuuY1r5ivJPZecbmcBMVQPvwxi2sR57WRjopZoIRA8l9l2ortaoIsTYOmetXyoXfwIoDm4iB04ZP/4VWlq5Hcmq3412VhPo1qx40tfvCWcF5djEpnXShFX7e6MLkjfLgFym1WEtOJJo9TAlfcTdnrRpjv1Yp4cIDdaTBDeWnVAe8u7/RfiIBK8Rj4JSQ6elHtblDMEEfq3~1; _ALGOLIA=anonymous-0d5361e2-bb11-469f-b7aa-15272d569358; dtCookie=v_4_srv_8_sn_2OSBROA0MJ8UHSPIF6RAI7SHA3NLFC5U_app-3Ab9702d2cec8810b9_1_ol_0_perc_100000_mul_1; rxVisitor=17170608451271NU585H95JA5441Q0H00TIQ0UOOJ6K6T; dtPC=8$461372412_793h-vLRPKJGFIUHFUOQUBQJRFUHMLAGACWJEQ-0e0; rxvt=1717063172419|1717060845127; dtSa=-; _cq_duid=1.1717060845.cmM1U5CEsrkc0Kd9; _cq_suid=1.1717060845.KyfnMH1zjtLhB4cV; _cs_c=0; _cs_id=f770cb71-8f6a-a653-cfc1-50e2bf43f337.1717060845.1.1717061373.1717060845.1.1751224845863.1; _cs_s=34.0.0.1717063173663; scarab.visitor=%2241422F7BB79A40B7%22; OptanonConsent=isGpcEnabled=0&datestamp=Thu+May+30+2024+14%3A59%3A32+GMT%2B0530+(India+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f61812e4-c79f-4237-abac-5e45868b86f9&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IN%3BDL&AwaitingReconsent=false; ajs_anonymous_id=9af0c6d9-5d92-49b7-ad8d-0e964cd50240; OptanonAlertBoxClosed=2024-05-30T09:20:51.885Z; _gcl_au=1.1.2121841055.1717060852; _ga=GA1.1.1187245688.1717060846; _gid=GA1.3.807000556.1717060852; _ga_VXFM372VJS=GS1.1.1717060845.1.1.1717061373.19.0.0; _ga_E9W6WKDZGY=GS1.3.1717060853.1.1.1717061373.21.0.0; _fbp=fb.2.1717060854326.699607901; optimizelyEndUserId=oeu1717060854442r0.05671052278358091; peerius_sess=155891545517|3WiR-5A4OOB_5Hg6fQTagiJ-oyKD-xnBCl3dg56k3BA; peerius_user=cuid:121743354067|KxYdvQ7u1o1evxkRAW1xemb78wzNgoLoKUyvD0zNnm4; segment_anonymous_id=9af0c6d9-5d92-49b7-ad8d-0e964cd50240; _gat_UA-2579437-22=1; _dc_gtm_UA-2579437-22=1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Priority': 'u=1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get('https://www.usc.co.uk/stores/all', cookies=cookies, headers=headers)

soup=BS(response.content,"html.parser")

data=[]

def list_page(r):
    dat={}
    r=requests.get(r,headers=headers,cookies=cookies)
    soup=BS(r.content,"html.parser")
    try:
        name=soup.find("h1").text.strip()
    except:
        name=None
    
    try:
        address=",".join(soup.find("div",id="StoreDetailsText").find_all("div","StoreFinderList")[2].text.replace("\n","").replace("\r","").replace("                    ","").strip().split())
    except:
        address=None

    try:
        telephone=soup.find("div","BoldTitle").find("span").next.next.text.replace("\r","").replace("\n","").strip()
    except:
        telephone=None

    try:
        d={}
        for k in soup.find("div","col-xs-12 col-md-6 Storesecondcollum").find_all("span")[1:]:
            abb=(k.text)
            d.update({abb.split(":")[0]:":".join(abb.split(":")[1:])})
        
    except:
        d=None

    dat.update({"NAME":name,"ADDRESS":address,"TELEPHONE":telephone})
    dat.update(d)
    data.append(dat)
    print(len(data))





l=[]
for i in soup.find("table",id="allStoresTable").find_all("tr"):
    for j in (i.find_all("td")):
        for k in j.find_all("a"):
            if "https://www.usc.co.uk"+k.get("href").replace("..","") not in l:
                l.append("https://www.usc.co.uk"+k.get("href").replace("..",""))


for r in l:
    try:
        list_page(r)
    except Exception as e:
        print(e)

        
df=pd.DataFrame(data)
df.to_excel("USC.xlsx",index=False)
