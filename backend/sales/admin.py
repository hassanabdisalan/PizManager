from django.contrib import admin
from .models import Sale

class SaleAdmin(admin.ModelAdmin):
    readonly_fields = ('grand_total_price',)
    list_display = ('customer', 'sale_date', 'grand_total_price')
    fieldsets = (
        (None, {
            'fields': ('customer', 'product1', 'quantity1', 'selling_price1', 'total_price1',
                       'product2', 'quantity2', 'selling_price2', 'total_price2', 'grand_total_price')
        }),
    )

admin.site.register(Sale, SaleAdmin)