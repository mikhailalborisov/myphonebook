from django.contrib import admin
from .models import PhoneBook


# Register your models here.
@admin.register(PhoneBook)
class DPhoneBookAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "note", "phone", "favourites", "date_of_creation")
    search_fields = ("first_name", "last_name", "note",)
    list_filter = ("favourites",)
    ordering = ("-favourites", "last_name",)
