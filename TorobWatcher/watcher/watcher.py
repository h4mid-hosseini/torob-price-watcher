import requests
from bs4 import BeautifulSoup
import json
from . import models
from django.core.mail import send_mail



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
                

                if lowest_offer < product.notice_price and lowest_offer != product.last_price:
                    product.last_price = lowest_offer
                    product.save()
                    email_body = f'The Price Is What You Want for {product.title}!'
                    send_mail("check out the new price detected!", email_body, 'sample@yourdomain.com', ['reciver@theirdomain.com'], fail_silently=False)
                    models.WatchDogBark.objects.create(title='your demanded price is available!', product=product, price=lowest_offer)
    
    return