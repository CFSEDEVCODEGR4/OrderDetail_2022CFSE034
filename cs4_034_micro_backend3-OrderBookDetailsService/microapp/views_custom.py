from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

import json

from microapp.models import Order
from microapp.serializers import OrderSerializer

#============================================================================================
# Order creation using custom endpoint
#============================================================================================
@api_view(['POST'])
def CreateOrder(request):
	if request.method == 'POST':
	
		new_order_request = JSONParser().parse(request)

		o_id = new_order_request['order_id']
		book_id = new_order_request['book_id']
		order_date = new_order_request['order_date']
		delivery_date = new_order_request['delivery_date']
		user_id = new_order_request['user_id']
		contact_no = new_order_request['contact_no']
		order_status = new_order_request['order_status'],
		item_count = new_order_request['item_count'],
		total_amount = new_order_request['total_amount'],
		total_discount = new_order_request['total_discount'],
		tax = new_order_request['tax'],
		net_amount = new_order_request['net_amount']

		if o_id is not None and book_id is not None and user_id is not None:	

			# Check if order_id already exists
			orders = Order.objects.all()
			orders = orders.filter(order_id = o_id)
			if (len(orders) > 0):
				return JsonResponse({'message': 'Order already exists.'}, status=status.HTTP_204_NO_CONTENT)
		 	
			# Create Order
			serializer_order = OrderSerializer(data=new_order_request)
		
			if serializer_order.is_valid():
				serializer_order.save()	
				return JsonResponse(serializer_order.data, status=status.HTTP_201_CREATED) 
			else:
				return JsonResponse(serializer_order.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			return JsonResponse({'message': 'Mandatory details missing.'}, status=status.HTTP_204_NO_CONTENT)  
	else:
		return JsonResponse({'message': 'Request method error'}, status=status.HTTP_204_NO_CONTENT)  
	
	

