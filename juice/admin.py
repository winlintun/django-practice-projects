from django.contrib import admin
from .models import Juice, Order


class JuiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "description"]
    list_filter = ["name", "description"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "description"]


admin.site.register(Juice, JuiceAdmin)
admin.site.register(Order)
