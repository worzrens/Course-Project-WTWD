from django.urls import path, include
from rest_framework import routers

from ecommerce.views import SellerViewSet, OfferItemViewSet, OfferItemSearchViewSet

router = routers.DefaultRouter()
router.register(r'sellers', SellerViewSet)
router.register(r'offers', OfferItemViewSet)
router.register(r'offers-search', OfferItemSearchViewSet)


urlpatterns = [
    path('', include(router.urls)),
]