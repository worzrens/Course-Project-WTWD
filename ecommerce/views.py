from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.response import Response

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


class OfferItemSearchViewSet(viewsets.ModelViewSet):
    queryset = OfferItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OfferItemListSerializer

    def list(self, request):
        request_filters = request.query_params
        print(request_filters)

        filter_query = Q(name__contains=request_filters.get('name'))

        queryset = OfferItem.objects.filter(filter_query)
        serializer = OfferItemListSerializer(queryset, many=True)
        return Response(serializer.data)


