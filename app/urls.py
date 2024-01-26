from django.urls import path
from .views import display_menu, place_order

urlpatterns = [
    path('home/', display_menu, name='menu'),
    path('place_order/<str:customer_name>/<str:order_items>/', place_order, name='place_order'),
    # Adicione mais URLs conforme necessário
]
