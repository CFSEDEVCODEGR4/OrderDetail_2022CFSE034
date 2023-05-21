from django.db import models
from django.urls import reverse


# Order Model
class Order(models.Model):    
    order_id = models.CharField(max_length = 15)                                        #Example: OID2300001
    book_id = models.CharField(max_length = 15)                                         #Example: RID001
    order_date = models.DateField(null=True, blank=False)                               #Example: 2023-02-02
    delivery_date = models.DateField(null=True, blank=False)                            #Example: 2023-02-02
    user_id = models.CharField(max_length = 15)                                         #Example: UID001
    contact_no = models.CharField(max_length = 10)                                      #Example: 9812398123
    ORDER_STATUS = (
            ('0' , 'pending'),                      
            ('2' , 'Confirmed'),                  
            ('3' , 'Rejected'),                 
            ('4' , 'Rejected'),                  
            ('6' , 'Delivered'),
            ('7' , 'Delivery Failed'),
            ('8' , 'Cancelled'),            
        )
    order_status = models.CharField(max_length = 2,choices=ORDER_STATUS,blank=False,default='0') 
    item_count = models.IntegerField(default=0)                                         #Example: 4
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)                  #Example: 300:50
    total_discount = models.DecimalField(max_digits=6, decimal_places=2)                #Example: -40:00
    tax = models.DecimalField(max_digits=6, decimal_places=2)                           #Example:  20:00
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)                    #Example: 280:50

    class Meta:
        ordering = ['order_id']

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])   
        
    def __str__(self):
        return self.order_id 







