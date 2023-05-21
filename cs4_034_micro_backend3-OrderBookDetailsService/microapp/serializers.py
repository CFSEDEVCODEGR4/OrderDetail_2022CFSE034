from rest_framework import serializers
from microapp.models import Order

# ============================================================
# Order
# ============================================================
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id',
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
                  ]  


