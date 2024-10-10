from django.contrib import admin
from .models import Stock

# Register your models here.
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'current_price', 'last_updated')
