from django.contrib import admin

from .models import Order

# =======================================================
# Controls the fields to display in admin panel
# =======================================================


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'order_id', 
                    'book_id', 
                    'order_date', 
                    'delivery_date', 
                    'user_id',
                    'contact_no', 
                    'order_status', 
                    'item_count', 
                    'total_amount',
                    'total_discount', 
                    'tax', 
                    'net_amount'
                    )

admin.site.register(Order, OrderAdmin)                    

