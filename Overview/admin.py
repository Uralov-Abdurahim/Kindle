from django.contrib import admin
from Overview.models import Overview

@admin.register(Overview)
class OverviewAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'sub_title')
    list_display_links = ('icon', 'title', 'sub_title')