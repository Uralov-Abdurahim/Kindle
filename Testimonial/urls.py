from django.urls import path
from Testimonial.views import TestimonialView

urlpatterns = [
    path('testimonial/', TestimonialView.as_view()),
]