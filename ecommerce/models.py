from django.db import models

from ecommerce.utils import OFFERS_CATEGORIES


class Seller(models.Model):
    company_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=40)
    on_site_since = models.IntegerField(default=0)


class OfferItem(models.Model):
    name = models.CharField(max_length=50)
    seller = models.ForeignKey(Seller, related_name='offer', on_delete=models.CASCADE)
    price = models.FloatField()
    count = models.IntegerField()
    release_date = models.DateField()
    category = models.CharField(max_length=5, choices=OFFERS_CATEGORIES)
