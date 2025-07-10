from django.urls import path
from Contact.views import ContactCreateAPIView

urlpatterns = [
    path('contact/', ContactCreateAPIView.as_view())
]