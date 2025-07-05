from django.urls import path
from About.views import AboutApiView

urlpatterns = [
    path('about/', AboutApiView.as_view()),
]