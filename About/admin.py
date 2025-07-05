from django.contrib import admin
from About.models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'text')
    list_display_links = ('image', 'title', 'text')