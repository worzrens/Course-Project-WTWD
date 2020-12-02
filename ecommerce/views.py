from rest_framework import viewsets, permissions

from ecommerce.models import Seller, OfferItem
from ecommerce.serializer import SellerSerializer, SellerListSerializer, OfferItemListSerializer, OfferItemSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return {
            'list': SellerListSerializer,
            'retrieve': SellerSerializer,
        }.get(self.action, SellerListSerializer)


class OfferItemViewSet(viewsets.ModelViewSet):
    queryset = OfferItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return {
            'list': OfferItemListSerializer,
            'retrieve': OfferItemSerializer,
        }.get(self.action, OfferItemListSerializer)

