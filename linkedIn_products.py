from msilib import schema
from operator import truediv
import requests
from bs4 import BeautifulSoup

url = "https://www.linkedin.com/services/api/products/searchResults"
product_list = []

querystring = {"start":0}


headers = {
    'cookie': '',  #  Put your cookies here 
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'csrf-token': "ajax:3750630049426296780",
    'referer': "https://www.linkedin.com/products/search/?q&trk=products_seo_search",
    'sec-ch-ua-mobile': "?0",
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }


for i in range(1,11):
    response = requests.request("GET", url, headers=headers, params=querystring)

    html = BeautifulSoup(response.text, 'html.parser')
    products = html.select('div.product-serp-card')
    for product in products:
        name = product.select('h3')[0].get_text().strip()
        company = product.select('h4')[0].get_text().strip()
        description = product.select('a.product-serp-card__description')[0].get_text().strip()

        schema = {
            'Name':name,
            'Company':company,
            'Description':description
        }
        print(schema)
        product_list.append(schema)
    querystring['start'] += 10

print(f"Total records are {len(product_list)}")        


