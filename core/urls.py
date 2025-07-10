from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('About.urls')),
    path('', include('Testimonial.urls')),
    path('', include('Overview.urls')),
    path('', include('Price.urls')),
    path('', include('Contact.urls'))
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)