from django.urls import path
from .views import *

urlpatterns = [
    path('home/', DisplayMenuView.as_view(), name='menu'),
    path('place_order/<str:customer_name>/<str:order_items>/', PlaceOrderView.as_view(), name='place_order'),
    path('pickup_order/<int:order_id/', PickUpOrderView.as_view(), name='pickup_order'),
    path('deliver_order/<int:order_id>/', DeliverOrderView.as_view(), name='deliver_order'),
    path('modify_order/<int:order_id>/', ModifyOrderView.as_view(), name='modify_order'),
    path('cancel_order/<int:order_id>/', CancelOrderView.as_view(), name='cancel_order'),
]
