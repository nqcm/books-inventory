
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Book, CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = (
        "title", "genre", "year", "created_date", "updated_date",
    )
    list_display = (
        "title", "genre", "year", "created_date", "updated_date",
    )
    readonly_fields = (
        "created_date", "updated_date",
    )