from django.urls import path
from .views import ProductsListView, InvoiceListView, TablesListView, CustomerListView, SalesOrderListView, AttendanceListView

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products-list'),
    path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
    path('sales-orders/', SalesOrderListView.as_view(), name='sales-orders-list'),
    path('customers/', CustomerListView.as_view(), name='customers-list'),
    path('tables/', TablesListView.as_view(), name='tables-list'),
    path('invoices/', InvoiceListView.as_view(), name='invoices-list'), 
]
