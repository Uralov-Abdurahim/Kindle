from django.urls import path
from Price.views import PriceView

urlpatterns = [
    path('price/', PriceView.as_view(), name='price')
]