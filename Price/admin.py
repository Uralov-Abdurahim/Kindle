from django.contrib import admin
from Price.models import Price

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'sub_title')
    list_display_links =  ('title', 'cost', 'sub_title')