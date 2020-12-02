import os
from datetime import datetime
from random import choice, randint, uniform

import django


def populate():
    print('Starting population script...')

    sellers = [
        Seller.objects.get_or_create(company_name=name, phone_number='123', address='123', on_site_since=randint(1,10))[0]
        for name in ['Seller 1', 'Seller 2', 'Seller 3']
    ]

    offer_items = [
        OfferItem.objects.get_or_create(
            name=f'Offer {randint(1000, 9999)}',
            seller=seller,
            price=uniform(100.0, 1000.0),
            count=randint(50, 100),
            release_date=datetime.now(),
            category=choice([category[0] for category in OFFERS_CATEGORIES]),
        )[0]
        for seller in sellers
    ]

    print('Done!')


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
    django.setup()

    from ecommerce.models import Seller, OfferItem
    from ecommerce.utils import OFFERS_CATEGORIES

    populate()
