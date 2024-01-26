from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    order_items = models.JSONField()
    status = models.CharField(max_length=50, default="Placed")
