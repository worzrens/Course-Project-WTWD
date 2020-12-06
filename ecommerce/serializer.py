from rest_framework import serializers

from ecommerce.models import Seller, OfferItem
from ecommerce.utils import OFFERS_CATEGORIES


class CustomChoiceField(serializers.ChoiceField):
    def to_representation(self, data):
        if data not in self.choices.keys():
            self.fail('invalid_choice', input=data)
        else:
            return self.choices[data]

    def to_internal_value(self, data):
        for key, value in self.choices.items():
            if value == data:
                return key
        self.fail('invalid_choice', input=data)


class SellerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['company_name', 'on_site_since']


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['company_name', 'on_site_since', 'phone_number', 'address']


class OfferItemSerializer(serializers.ModelSerializer):
    category = CustomChoiceField(choices=OFFERS_CATEGORIES)
    seller = SellerListSerializer(read_only=True)

    class Meta:
        model = OfferItem
        fields = ['name', 'seller', 'price', 'count', 'release_date', 'category', ]


class OfferItemListSerializer(serializers.ModelSerializer):
    category = CustomChoiceField(choices=OFFERS_CATEGORIES)

    class Meta:
        model = OfferItem
        fields = ['id', 'name', 'price', 'category']