import requests
from bs4 import BeautifulSoup as BS


    # url = "https://www.yellow-pages.ph/search/warehouse/nationwide/page-1"

def crawl_list_page(url):
    r = requests.get(url)
    soup = BS(r.text,'html.parser')
    listing = soup.find_all('div','search-listing')
    products = []
    for i in listing:
        title = i.find('h2')
        try:
            title = title.text.strip()
        except:
            title = "Not Available"
        try:
            product_url = 'https://www.yellow-pages.ph'+i.find('a').get('href')
        except:
            product_url = "Not Available"

        try:
            address = i.find('div','search-busines-address').text.strip()
        except:
            address = "Not Available"
        try:
            timing = i.find('div','search-busines-time').text.strip()
        except:
            timing = "Not Available"

        try:
            phone_number = i.find('a',attrs={'data-section':'contact number'}).get('data-phone')
        except:
            phone_number = "Not Available"
        products.append({
            'title':title,
            'product_url':product_url,
            'address':address,
            'timing':timing,
            'phone':phone_number
        })
    return products

# print(products)


url = "https://www.yellow-pages.ph/search/data-entry/nationwide/page-1"
# for i in urls:
products = crawl_list_page(url)
print(products)
