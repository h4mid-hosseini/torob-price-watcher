from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from bs4 import BeautifulSoup
import requests
import json

from . import models




def release_dogs():
    products = models.WatchingProducts.objects.all()

    if products.first != None:

        for product in products:
            try:
                response = requests.get(product.url)
                soup = BeautifulSoup(response.content, 'html.parser')
                json_ld_script = soup.find('script', type='application/ld+json')

                if json_ld_script:
                    json_data = json_ld_script.string
                    data = json.loads(json_data)
                    lowest_offer = int(data.get('offers')['lowPrice'])
                    
                    print(lowest_offer, lowest_offer < product.notice_price)
                    print(product.last_price, lowest_offer != product.last_price)
                    if lowest_offer < product.notice_price and lowest_offer != product.last_price:
                        subject = 'Check out the new price detected!'
                        from_email = 'notification@h4mid-hosseini.ir'
                        to_email = [product.email_address]

                        # Render the HTML content using the template
                        html_content = render_to_string('emails/watcher.html', {
                            'product': product,
                            'lowest_offer': lowest_offer,
                            'current_datetime': timezone.now(),  # Assuming you have imported timezone
                        })

                        # Create and send the email
                        msg = EmailMultiAlternatives(subject, '', from_email, to_email)
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()


                        models.WatchDogBark.objects.create(title='your demanded price is available!', product=product, price=lowest_offer)
                        product.last_lowest_price = lowest_offer

                    product.last_price = lowest_offer
                    product.save()
            
            except Exception as e:
                print(f'An error on watching. detail: {e}','\n')
    return