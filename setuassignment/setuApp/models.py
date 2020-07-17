from django.db import models

# Create your models here.
class FetchBill(models.Model):
    customer_name = models.CharField(max_length=200, blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    due_amount = models.FloatField()
    ref_id = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)