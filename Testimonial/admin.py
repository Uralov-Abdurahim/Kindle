from django.contrib import admin
from Testimonial.models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('sentences', 'image', 'name', 'position')
    list_display_links = ('sentences', 'image', 'name', 'position')