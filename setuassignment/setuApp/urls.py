from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/fetch-bill', views.fetchCustomerBill.as_view(), name='get-folio-by-pan-api'),
    url('api/v1/payment-update', views.updateCustomerBill.as_view(), name = 'update-customer-bill')
]
