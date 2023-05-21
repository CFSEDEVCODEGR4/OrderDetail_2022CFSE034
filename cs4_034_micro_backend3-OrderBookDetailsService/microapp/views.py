from django.shortcuts import render

from rest_framework import generics
from microapp.serializers import  OrderSerializer
from microapp.serializers import  Order

# ===================================================
# Order
# ===================================================

class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        queryset = Order.objects.all()
        user = self.request.query_params.get('user_id', None)
        book = self.request.query_params.get('book_id', None)
        status = self.request.query_params.get('order_status', None)
        order = self.request.query_params.get('order_id', None)
        if (user is not None):
            queryset = queryset.filter(user_id = user)
        if (book is not None):
            queryset = queryset.filter(book_id = rest)
        if (status is not None):
            queryset = queryset.filter(order_status = status)
        if (order is not None):
            queryset = queryset.filter(order_id = order)
        return queryset

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# ===================================================

