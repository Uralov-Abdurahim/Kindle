from django.contrib import admin
from Contact.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_display_links = ('name', 'email', 'message')
    search_fields = ('name', 'email')