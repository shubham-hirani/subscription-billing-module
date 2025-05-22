from django.urls import path

from .views import subscribe, unsubscribe, invoice_list, pay_invoice

urlpatterns = [path('subscribe/', subscribe),
               path('unsubscribe/', unsubscribe),
               path('invoice_list/', invoice_list),
               path('pay_invoice/', pay_invoice), ]
