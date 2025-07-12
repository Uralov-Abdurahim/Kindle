from django.contrib import admin
from Home.models import Home

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'sub_title', 'file')
    list_display_links = ('image', 'title', 'sub_title', 'file')