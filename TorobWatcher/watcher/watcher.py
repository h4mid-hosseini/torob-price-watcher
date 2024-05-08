import requests
from bs4 import BeautifulSoup
import json
from . import models

products = models.WatchingProducts.objects.all()

def release_dogs():
    if products.first != None:
        for product in products:
            response = requests.get(product.url)

            soup = BeautifulSoup(response.content, 'html.parser')

            json_ld_script = soup.find('script', type='application/ld+json')

            if json_ld_script:
                json_data = json_ld_script.string
                
                data = json.loads(json_data)
                
                lowest_offer = int(data.get('offers')['lowPrice'])
                
                if lowest_offer != product.last_price:
                    product.last_price = lowest_offer
                    product.save()

                if lowest_offer < product.notice_price:
                    models.WatchDogBark.objects.create(title='price is what you want', product=product, price=lowest_offer)
