
class Crawl:
    def __init__(self,url) -> None:
        response = requests.post(url, headers=headers, json=json_data)
        if response.status_code==200:
            js=response.json()
            result = self.get_links(js)
            print(result)


    def get_links(self,js):
        
        data=[]
        while len(data)<=500:
            response = requests.post(url, headers=headers, json=json_data)
            js=response.json()
            for i in js["data"]["channel"]["channel_videos_all_videos"]["edges"]:
                if(len(data) == 500):
                    df=pd.DataFrame(data)
                    df.to_excel("T-series.xlsx",index=False)
                    return df
                title=(i["node"]["title"])
                links=("https://www.dailymotion.com/video/"+i["node"]["xid"])
                data.append({"TITLE":title,"LINKS":links})
            json_data['variables']["page"]+=1






url='https://graphql.api.dailymotion.com/'
crl=Crawl(url)
