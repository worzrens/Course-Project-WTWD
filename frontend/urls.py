from django.urls import path
from . import views

urlpatterns = [
    path('', views.tech),
    path('cloth/', views.cloth),
    path('home/', views.home),
    path('profile/', views.profile),
    path('offer/<int:id>', views.offer_info),
]