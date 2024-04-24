import requests

from bs4 import BeautifulSoup as BS
import time
import pandas as pd

def fetch_data(url):
    r=requests.get(url)
    if r.status_code==200:
        soup=BS(r.content,"html.parser")
        get_link_from_main_page(soup) 


def get_link_from_main_page(soup):
    l=[]
    for i in soup.find("section",attrs={"id":"quick-search"}).find_all("a"):
        if i.get("href")=="https://people.yellowpages.com/whitepages":
            continue
        else:
            l.append("https://www.yellowpages.com"+i.get("href"))
    parse_main_page_links(l)


def parse_main_page_links(l):
    list1=[]
    for i in l:
        r=requests.get(i)
        soup=BS(r.content,"html.parser")
        list_page(soup,list1)
    


def list_page(soup,list1):
    l1=[]
    for i in soup.find("div","search-results organic").find_all("div","v-card"):
        link=i.find("a")
        l1.append("https://www.yellowpages.com"+link.get("href"))
    pasrse_list_page_link(l1,list1)


def pasrse_list_page_link(l1,list1):
    for i in l1:
        r2=requests.get(i)
        soup=BS(r2.content,"html.parser")
        tit=title(soup)
        cat=categories(soup) 
        pho=phone_no(soup)
        lin=website_link(soup)
        d={}
        d["Title"]=tit
        d["Categories"]=cat
        d["Phone"]=pho
        d["Links"]=lin
        list1.append(d)
    df=pd.DataFrame(list1)
    df.to_excel("yellow.xlsx",index=False)
        

def title(soup):
    try:
        title=soup.find("div","sales-info").find("h1").text
    except:
        title="Not available"
    return title

def categories(soup):
    try:
        categories=soup.find("div","categories").text
    except:
        categories="Not available"
    return categories

def phone_no(soup):
    try:
        phone_no=soup.find("section",attrs={"id":"default-ctas"}).find("a").text
    except:
        phone_no="Not available"
    return phone_no

def website_link(soup):
    try:
        link=soup.find("section",attrs={"id":"default-ctas"}).find("a","website-link dockable").get("href")
    except:
        link="Not available"
    return link


url=("https://www.yellowpages.com/")
fetch_data(url)
