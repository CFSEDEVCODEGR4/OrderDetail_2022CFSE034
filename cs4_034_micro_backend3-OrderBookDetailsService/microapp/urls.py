from django.urls import path
from microapp import views
from microapp import views_custom



from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Swagger API docs",
      default_version='v1',
      description="Swagger API docs description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

#============================================================================
# API URL  http://127.0.0.1:8000/microapp/
#============================================================================
urlpatterns = [         

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),    

   # =============
    # Orders
    # =============
    path('api/orders/', views.OrderList.as_view()),                           
    path('api/orders/<int:pk>', views.OrderDetail.as_view()),  
    path('api/orders/create_order/', views_custom.CreateOrder),  

           

] 
