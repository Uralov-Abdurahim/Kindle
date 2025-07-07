from django.urls import path
from Overview.views import OverviewAPI

urlpatterns = [
    path('overview/', OverviewAPI.as_view(), name='overviews')
]