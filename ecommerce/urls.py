from django.urls import path, include
from rest_framework import routers

from ecommerce.views import SellerViewSet, OfferItemViewSet

router = routers.DefaultRouter()
router.register(r'sellers', SellerViewSet)
router.register(r'offers', OfferItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]